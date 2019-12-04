import youtube_dl

def download_audio(video, format_='mp3', bitrate='192'):
    download_opt = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec' : format_,
            'preferredquality' : bitrate
        }]}
    with youtube_dl.YoutubeDL(download_opt) as dl:
        print(f'Downloading audio for {video}')
        dl.download([video])
download_audio('https://www.youtube.com/watch?v=KTknN6MFKqg')