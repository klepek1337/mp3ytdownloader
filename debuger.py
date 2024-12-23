import subprocess
import sys
import os

def run_command(command):
    """Uruchamia polecenie w terminalu i zwraca wynik."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        print(f"\nCommand: {' '.join(command)}")
        print(f"Output:\n{result.stdout}")
        if result.stderr:
            print(f"Errors:\n{result.stderr}")
        return result.stdout, result.stderr
    except Exception as e:
        print(f"Error running command: {e}")
        return None, str(e)

def check_ffmpeg():
    """Sprawdza, czy `ffmpeg` jest poprawnie zainstalowany."""
    print("Checking ffmpeg installation...\n")
    run_command(["ffmpeg", "-version"])

def check_yt_dlp():
    """Sprawdza, czy `yt-dlp` jest poprawnie zainstalowany."""
    print("Checking yt-dlp installation...\n")
    try:
        result = subprocess.run(["yt-dlp", "--version"], capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            print(f"yt-dlp version: {result.stdout.strip()}")
        else:
            print("yt-dlp is not installed or not in the system PATH.")
            sys.exit(1)  # Zakończ skrypt, jeśli `yt-dlp` nie jest zainstalowane.
    except FileNotFoundError:
        print("yt-dlp is not found in the system PATH.")
        sys.exit(1)  # Zakończ skrypt, jeśli `yt-dlp` nie jest zainstalowane.

def list_formats(video_url):
    """Wyświetla listę dostępnych formatów dla danego URL."""
    print("\nListing available formats...")
    run_command(["yt-dlp", "-F", video_url])

def download_best(video_url):
    """Pobiera najlepszy format wideo i audio, łącząc je."""
    print("\nDownloading best video + audio...")
    run_command(["yt-dlp", "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best", "--verbose", video_url])

def download_metadata(video_url):
    """Pobiera tylko metadane wideo."""
    print("\nDownloading video metadata...")
    run_command(["yt-dlp", "--dump-json", video_url])

def debug_video(video_url):
    """Pełny proces debugowania."""
    print(f"Starting debug process for URL: {video_url}\n")
    
    # Check if ffmpeg is installed
    check_ffmpeg()
    
    # Check if yt-dlp is installed
    check_yt_dlp()
    
    # List available formats
    list_formats(video_url)
    
    # Download metadata
    download_metadata(video_url)
    
    # Download best video + audio
    download_best(video_url)

if __name__ == "__main__":
    # Wprowadź link do wideo tutaj:
    VIDEO_URL = "https://www.youtube.com/watch?v=3QpX8hOqGB8&list=PL0udCJ3wnFVAZFi-B3-9Gh-7Jmr7z7xVI&index=4&ab_channel=GeorgianaLobont"
    
    # Rozpocznij debugowanie
    debug_video(VIDEO_URL)
