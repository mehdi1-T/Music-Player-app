import requests
import pygame
import os

pygame.init()
pygame.mixer.init()

play_state = False
current_song = None  # track what's loaded
def get_music(song):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36"
    }

    url = f"https://api.deezer.com/search?q={song}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    if not data.get("data"):
        raise ValueError(f"No results found for: {song}")

    preview_url = data["data"][0]["preview"]

    # ✅ Stream the download so it doesn't fail silently
    audio_response = requests.get(preview_url, headers=headers, stream=True)
    audio_response.raise_for_status()

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    music_dir = os.path.join(BASE_DIR, "music")
    os.makedirs(music_dir, exist_ok=True)
    filepath = os.path.join(music_dir, f"{song}.mp3")

    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    try:
        pygame.mixer.music.unload()
    except AttributeError:
        pass

    # ✅ Write in chunks
    with open(filepath, "wb") as f:
        for chunk in audio_response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    # ✅ Verify file actually has content
    if os.path.getsize(filepath) == 0:
        raise RuntimeError("Downloaded file is empty — Deezer may have blocked the request")

    print(f"✅ Downloaded to: {filepath} ({os.path.getsize(filepath)} bytes)")
    pygame.mixer.music.load(filepath)
def play_song(song_name):
    global play_state, current_song

    if play_state and song_name == current_song:
        # Same song is playing — stop it
        pygame.mixer.music.stop()
        play_state = False
    else:
        # New song or nothing playing — load and play
        get_music(song_name)
        pygame.mixer.music.play()
        play_state = True
        current_song = song_name