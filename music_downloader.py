from pytube import YouTube # type: ignore

# Read the list of YouTube URLs from a file
with open('youtube_urls.txt', 'r') as f:
    urls = f.readlines()

# Create a new folder in the download folder
download_folder = 'downloads/youtube_music'
import os
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Download each video and extract the audio
for url in urls:
    # Remove the newline character from the URL
    url = url.strip()

    # Create a YouTube object for the URL
    yt = YouTube(url)

    # Get the audio stream with the highest quality available
    audio_stream = yt.streams.filter(type='audio').get_highest_resolution()

    # Download the audio stream to the download folder
    audio_stream.download(download_folder, filename=f'{yt.title}.mp3')

print('All music downloaded successfully.')