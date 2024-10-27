import openai
import requests
import re


GENIUS_ACCESS_TOKEN = "___wtySd5Smh8UPQLWwGRkguQjQQ5yZ7ONrrm31ZgK-m3bpc3tYdFtva07KRQHL8"
openai.api_key = "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"

def parse_artists(artist_name):
    
    artists = re.split(r',|\band\b', artist_name, flags=re.IGNORECASE)
    return ', '.join(artist.strip() for artist in artists)

def get_song_id(song_name, artist_name):
    
    formatted_artist_name = parse_artists(artist_name)
    search_url = "https://api.genius.com/search"
    headers = {"Authorization": f"Bearer {GENIUS_ACCESS_TOKEN}"}
    params = {"q": f"{song_name} {formatted_artist_name}"}
    response = requests.get(search_url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data["response"]["hits"]:
            song_id = data["response"]["hits"][0]["result"]["id"]
            return song_id
        else:
            print("Song not found on Genius. Please check the song name and artist.")
    else:
        print(f"Error: {response.status_code}")
    return None

def get_song_samples(song_id):
  
    song_url = f"https://api.genius.com/songs/{song_id}"
    headers = {"Authorization": f"Bearer {GENIUS_ACCESS_TOKEN}"}
    response = requests.get(song_url, headers=headers)
    
    if response.status_code == 200:
        song_data = response.json()
        samples = song_data["response"]["song"].get("sampled_music", [])
        
        if samples:
            sampled_data = {}
            for i, sample in enumerate(samples, start=1):
                sample_title, sample_artist = sample["full_title"].split(" by ")
                sampled_data[f"sampled_song_{i}"] = sample_title.strip()
                sampled_data[f"sampled_artist_{i}"] = sample_artist.strip()
            return sampled_data
        else:
            print("No samples found on Genius. Checking with OpenAI...")
            return None  
    else:
        print(f"Error retrieving song samples: {response.status_code}")
        return None

def query_openai_for_samples(song_name, artist_name):
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a knowledgeable assistant that provides information on song samples in the exact format 'Samples: Song by Artist'."},
            {"role": "user", "content": f"List any known samples used in the song '{song_name}' by {artist_name} in this exact format: 'Samples: Song by Artist'."}
        ],
        max_tokens=150
    )
    
    samples_info = response['choices'][0]['message']['content']
    return parse_openai_samples(samples_info)

def parse_openai_samples(samples_info):
    
    sampled_data = {}
    
    lines = samples_info.split('\n')
    for i, line in enumerate(lines, start=1):
        if "by" in line:
            sample_title, sample_artist = line.split(" by ")
            sampled_data[f"sampled_song_{i}"] = sample_title.replace("Samples:", "").strip()
            sampled_data[f"sampled_artist_{i}"] = sample_artist.strip()
    return sampled_data

def main():
    print("Enter the song details to find its samples.")
    song_name = input("Song name: ")
    artist_name = input("Artist name (use commas or 'and' to separate multiple artists): ")

    song_id = get_song_id(song_name, artist_name)
    if song_id:
        sampled_data = get_song_samples(song_id)
        
        if sampled_data:
            
            for key, value in sampled_data.items():
                print(f"{key} = \"{value}\"")
        else:
            
            sampled_data = query_openai_for_samples(song_name, artist_name)
            print("Samples (from OpenAI):")
            for key, value in sampled_data.items():
                print(f"{key} = \"{value}\"")
    else:
        print("Song not found.")

if __name__ == "__main__":
    main()
