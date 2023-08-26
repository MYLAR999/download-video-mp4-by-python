from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=eE0FjN1F-2w"

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

download_path = r"Downloads"

stream.download(output_path=download_path)

print("Download complete thx.")