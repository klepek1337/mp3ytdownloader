import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def add_ffmpeg_to_path(ffmpeg_path):
    # Sprawdź, czy podana ścieżka istnieje
    if not os.path.exists(ffmpeg_path):
        print(f"Ścieżka '{ffmpeg_path}' nie istnieje. Upewnij się, że podałeś poprawny folder.")
        return

    # Pobierz bieżący PATH
    current_path = os.environ.get("PATH", "")
    
    # Sprawdź, czy ścieżka już jest w PATH
    if ffmpeg_path in current_path:
        print("Ścieżka już znajduje się w PATH.")
        return
    
    # Dodaj ścieżkę do zmiennych środowiskowych (tylko dla bieżącej sesji)
    os.environ["PATH"] = current_path + os.pathsep + ffmpeg_path
    print(f"Dodano '{ffmpeg_path}' do PATH dla tej sesji.")

    # Modyfikacja PATH w systemie (stała zmiana)
    try:
        subprocess.run(
            ['setx', 'PATH', f"{current_path};{ffmpeg_path}"],
            check=True,
            shell=True
        )
        print(f"Ścieżka '{ffmpeg_path}' została dodana do PATH globalnie.")
    except subprocess.CalledProcessError as e:
        print("Nie udało się zapisać ścieżki globalnie:", str(e))


def choose_folder():
    # Użyj tkinter do wyboru folderu
    root = tk.Tk()
    root.withdraw()  # Ukrywa główne okno
    folder_path = filedialog.askdirectory(title="Wybierz folder z FFmpeg")
    return folder_path


# Wybór folderu z FFmpeg
ffmpeg_path = choose_folder()

# Sprawdzenie, czy użytkownik wybrał folder
if ffmpeg_path:
    add_ffmpeg_to_path(ffmpeg_path)
else:
    print("Nie wybrano folderu.")
