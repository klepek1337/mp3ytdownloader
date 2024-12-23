import yt_dlp
import os

def download_playlist_as_mp4(playlist_url):
    # Путь к папке с ffmpeg.exe
    ffmpeg_path = r"C:\Users\zbido\Downloads\ffmpeg-2024-12-19-git-494c961379-full_build\ffmpeg-2024-12-19-git-494c961379-full_build\bin"

    # Проверяем, что ffmpeg.exe и ffprobe.exe находятся в указанной папке
    if not all(os.path.exists(os.path.join(ffmpeg_path, exe)) for exe in ['ffmpeg.exe', 'ffprobe.exe']):
        print("Не удалось найти ffmpeg.exe или ffprobe.exe по указанному пути!")
        return

    output_path = "Downloads"  # Папка для сохранения файлов
    os.makedirs(output_path, exist_ok=True)  # Создаем папку, если ее нет

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': os.path.join(output_path, '%(playlist_index)s - %(title)s.%(ext)s'),
        'quiet': False,
        'verbose': True,
        'merge_output_format': 'mp4',
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{'key': 'FFmpegMerger'}],
        'ignoreerrors': True,  # Игнорировать ошибки
        'retries': 2,  # Больше попыток
        'playlist_items': '1-2',  # Ограничение на загрузку первых 10 видео
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Загрузка плейлиста: {playlist_url}")
            ydl.download([playlist_url])
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    playlist_url = input("Введите URL плейлиста YouTube: ")
    download_playlist_as_mp4(playlist_url)
