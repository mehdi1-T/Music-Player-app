import os
import io
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image
import app.state as state


def get_song_packet(filepath):
    """Read MP3 tags and return a dict with title, artist, album, duration, album_art."""
    try:
        audio = MP3(filepath)
        tags  = ID3(filepath)
    except Exception:
        return {
            "title":     os.path.basename(filepath),
            "artist":    "Unknown Artist",
            "album":     "Unknown Album",
            "duration":  0.0,
            "max_pos":   0,
            "album_art": None,
        }

    duration  = audio.info.length
    album_art = None
    for key in tags.keys():
        if key.startswith("APIC"):
            album_art = Image.open(io.BytesIO(tags[key].data))
            break

    return {
        "title":     str(tags.get("TIT2", os.path.basename(filepath))),
        "artist":    str(tags.get("TPE1", "Unknown Artist")),
        "album":     str(tags.get("TALB", "Unknown Album")),
        "duration":  duration,
        "max_pos":   int(duration),
        "album_art": album_art,
    }


def load_songs_from_folder():
    """Scan music/ folder and add all audio files to the playlist."""
    if not os.path.exists(state.MUSIC_DIR):
        os.makedirs(state.MUSIC_DIR)
        return
    for fname in sorted(os.listdir(state.MUSIC_DIR)):
        if fname.lower().endswith((".mp3", ".wav", ".ogg", ".flac")):
            full_path = os.path.join(state.MUSIC_DIR, fname)
            if full_path not in state.playlist:
                state.playlist.append(full_path)