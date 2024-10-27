import requests
from bs4 import BeautifulSoup

def format_url(song_title, artist_name):
    formatted_artist = artist_name.replace(" ", "-")
    formatted_song = song_title.replace(" ", "-")
    return f"https://www.whosampled.com/{formatted_artist}/{formatted_song}/"

def get_samples(song_title, artist_name):
    song_url = format_url(song_title, artist_name)
    print(f"Generated URL: {song_url}")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    
    response = requests.get(song_url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        sample_sections = soup.find_all("section", class_="track-sample")
        samples = []

        for sample in sample_sections:
            sampled_song = sample.find("a", class_="trackName").text
            sampled_artist = sample.find("span", class_="trackArtist").text
            samples.append(f"{sampled_song} by {sampled_artist}")

        if samples:
            return "Samples used in this song:\n" + "\n".join(samples)
        else:
            return "No samples found for this song."

    elif response.status_code == 404:
        return "Error 404: The song or artist could not be found. Please check the spelling or try a different song."
    
    elif response.status_code == 403:
        return "Error 403: Access to this page is restricted. You may need special permissions to access this content."

    elif response.status_code == 500:
        return "Error 500: Internal server error. The server encountered an issue. Try again later."

    else:
        return f"Error {response.status_code}: An unexpected error occurred. Please try again."

def main():
    song_title = input("Enter the song title: ")
    artist_name = input("Enter the artist name: ")
    result = get_samples(song_title, artist_name)
    print(result)

if __name__ == "__main__":
    main()
