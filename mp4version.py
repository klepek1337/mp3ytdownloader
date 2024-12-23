import yt_dlp

def download_playlist_as_mp4(playlist_url):
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'Downloads\\%(playlist_index)s - %(title).40s.%(ext)s',
        'quiet': False,
        'verbose': True,
        'merge_output_format': 'mp4',
        'ffmpeg_location': r'C:\Users\fulek\Desktop\gigachad\ffmpeg-2024-12-19-git-494c961379-full_build\bin',
        'postprocessors': [
            {'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}
        ],
        'ignoreerrors': True,
        'retries': 3,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
    except Exception as e:
        print(f"Błąd podczas pobierania playlisty: {e}")

if __name__ == "__main__":
    playlist_url = "https://youtube.com/playlist?list=PLFXTLX9seZHjeRDbyq6mOKwfidLnNzew5&si=pCtoPnoFAXWC0nBE"
    download_playlist_as_mp4(playlist_url)

