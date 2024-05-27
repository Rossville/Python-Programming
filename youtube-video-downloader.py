from pytube import YouTube
import sys

# Check if the script received the correct number of arguments
if len(sys.argv) < 2:
    print("Usage: python script.py <YouTube_URL>")
    sys.exit(1)

link = sys.argv[1]
yt = YouTube(link)

print("Title :", yt.title)
print("Views :", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download()

print("downloaded....")