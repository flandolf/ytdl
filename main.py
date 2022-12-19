from pytube import Playlist, YouTube
import rm
# Replace PLAYLIST_URL with the URL of the YouTube playlist you want to download
playlist = Playlist('https://music.youtube.com/playlist?list=PLYFfG4QnfZqK6jKO243hABSsw685oGXoh')

# Print the list of videos in the playlist
print(playlist.video_urls)

# Iterate through the list of videos and download each one
for url in playlist.video_urls:
    # Use the YouTube() function to create a YouTube object for the video
    yt = YouTube(url)

    # Use the streams.first() method to retrieve the first stream that matches the specified file format and resolution
    # Replace 'mp4' with the desired file format (e.g. 'mp4', 'webm', '3gp')
    # Replace '720p' with the desired resolution (e.g. '720p', '360p', '1080p')
    stream = yt.streams.filter(file_extension='mp4', resolution='720p').first()
    # Download the video to a local directory called 'videos'
    stream.download('./videos')

    # Create an input stream from the video file
    video_file = './videos/' + stream.default_filename 
import os

# Replace './videos' with the path to the directory where the video files are stored
for file in os.listdir('./videos'):
    # Check if the file is a video file
    if file.endswith('.mp4'):
        # Use the os.system() function to run the ffmpeg command
        os.system('ffmpeg -i "./videos/' + file + '" "./videos/' + file[:-4] + '.mp3"')
rm.delete('./videos')