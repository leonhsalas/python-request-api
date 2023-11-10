import yt_dlp

url = "https://youtu.be/7OPg-ksxZ4Y"

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("video downloaded succesfully")