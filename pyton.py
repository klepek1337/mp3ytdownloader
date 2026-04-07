from codecs import ignore_errors
import yt_dlp
import os

def download_playlist_as_mp3(playlist_url):
    # Ścieżka do folderu z ffmpeg.exe
    ffmpeg_path = r"D:\Downloads\ffmpeg-2026-04-06-git-7fd2be97b9-full_build\bin"

    # Sprawdź, czy ffmpeg.exe i ffprobe.exe znajdują się w podanej ścieżce
    if not all(os.path.exists(os.path.join(ffmpeg_path, exe)) for exe in ['ffmpeg.exe', 'ffprobe.exe']):
        print("Nie znaleziono ffmpeg.exe lub ffprobe.exe w podanej ścieżce!")
        return

    output_path = "downloads"  # Folder, w którym będą zapisane pliki
    os.makedirs(output_path, exist_ok=True)  # Tworzy folder, jeśli nie istnieje

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(playlist_index)s - %(title)s.%(ext)s'),
        'quiet': False,
        'noplaylist': False,
        "ignoreerrors": True,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ],
        'ffmpeg_location': ffmpeg_path,  # Dodajemy ścieżkę do ffmpeg.exe
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Pobieranie playlisty: {playlist_url}")
        ydl.download([playlist_url])
        

if __name__ == "__main__":
    playlist_url = input("Podaj URL playlisty YouTube: ")
    download_playlist_as_mp3(playlist_url)
