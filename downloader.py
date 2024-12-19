import os
from yt_dlp import YoutubeDL

# Define the playlist URL and output directory
playlist_url = "https://www.youtube.com/playlist?list=PLEekr8MhjAeQtCjBrGNAKfsT-9ol969hb"
output_dir = "yt_music"
os.makedirs(output_dir, exist_ok=True)

# yt-dlp options for maximum performance and full resolution
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Full resolution
    'outtmpl': os.path.join(output_dir, '%(playlist_index)s - %(title)s.%(ext)s'),  # Organized filenames
    'merge_output_format': 'mp4',  # Output format
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',  # Ensure mp4 format
    }],
    'n_threads': 16,  # Use 16 threads for faster download (you can increase this depending on your system)
    'progress_hooks': [lambda d: print(f"Status: {d['status']} - {d.get('filename', '')}")],
    'concurrent_fragment_downloads': 4,  # Download 4 fragments concurrently per video
    'downloader': 'aria2c',  # Use aria2c for multi-source downloads (recommended for max performance)
    'postprocessor_args': [
        '-threads', '8',  # Enable multi-threading in FFmpeg postprocessing (adjust based on your CPU cores)
    ],
}

# Download playlist
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])
