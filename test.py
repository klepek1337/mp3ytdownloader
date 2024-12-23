import yt_dlp
import os

def download_playlist_as_mp4(playlist_url):
    # Ścieżka do folderu z ffmpeg.exe
    ffmpeg_path = r"C:\Users\zbido\Downloads\ffmpeg-2024-12-19-git-494c961379-full_build\ffmpeg-2024-12-19-git-494c961379-full_build\bin"

    # Sprawdź, czy ffmpeg.exe i ffprobe.exe znajdują się w podanej ścieżce
    if not all(os.path.exists(os.path.join(ffmpeg_path, exe)) for exe in ['ffmpeg.exe', 'ffprobe.exe']):
        print("Nie znaleziono ffmpeg.exe lub ffprobe.exe w podanej ścieżce!")
        return

    # Указываем путь для загрузки файлов
    output_path = r"C:\Users\zbido\Downloads\Colindele"  # Папка для сохранения файлов
    os.makedirs(output_path, exist_ok=True)  # Создаем папку, если её нет

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',  # Выбираем самое качественное видео и аудио
        'outtmpl': os.path.join(output_path, '%(playlist_index)s - %(title)s.%(ext)s'),  # Путь для сохранения файлов
        'quiet': False,
        'verbose': True,
        'merge_output_format': 'mp4',  # Формат для объединения видео и аудио
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',  # Используем FFmpeg для конвертации видео
            'preferredformat': 'mp4',  # Формат mp4
        }],
        'ignoreerrors': True,  # Игнорировать ошибки
        'noplaylist': False,  # Убедиться, что весь плейлист скачивается
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Загрузка плейлиста: {playlist_url}")
        ydl.download([playlist_url])

if __name__ == "__main__":
    playlist_url = input("Введите URL плейлиста YouTube: ")
    download_playlist_as_mp4(playlist_url)
