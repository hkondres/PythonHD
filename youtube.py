from pytube import YouTube

# Enter the video URL
url = input("Enter YouTube video URL: ")

# Create a YouTube object
yt = YouTube(url)

# Select the highest resolution video stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()
