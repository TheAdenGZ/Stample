import yt_dlp

def download_song(song, artist):
    # Format the search query
    query = f"{song} {artist}"
    
    # Set options for yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',  # or 'wav', 'aac', etc.
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Output file name
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Search and download the song
        ydl.download([f"ytsearch:{query}"])

