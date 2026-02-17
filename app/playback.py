import random
import pygame
from PIL import Image, ImageTk
import app.state as state
from app.packet import get_song_packet

# ui references — set by ui.py after widgets are created
song_title_widget  = None
artist_name_widget = None
time_start_widget  = None
time_end_widget    = None
progress_bar_widget = None
album_label_widget = None
mainImage_orig     = None


def fmt_time(seconds):
    seconds = max(0, int(seconds))
    return f"{seconds // 60}:{seconds % 60:02d}"


def load_and_play(index):
    if not state.playlist:
        return

    state.current_index  = index % len(state.playlist)
    filepath             = state.playlist[state.current_index]

    # Stop current, load and play new file
    pygame.mixer.music.stop()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play(0)   # 0 = play once

    state.current_packet = get_song_packet(filepath)
    state.total_duration = state.current_packet["duration"]
    state.is_playing     = True

    # Update UI labels
    if song_title_widget:
        song_title_widget.config(text=state.current_packet["title"])
    if artist_name_widget:
        artist_name_widget.config(text=state.current_packet["artist"])
    if time_start_widget:
        time_start_widget.config(text="0:00")
    if time_end_widget:
        time_end_widget.config(text=fmt_time(state.total_duration))

    # Update progress bar range
    if progress_bar_widget:
        progress_bar_widget.config(to=max(state.current_packet["max_pos"], 1))
        progress_bar_widget.set(0)

    # Update album art
    if album_label_widget:
        if state.current_packet["album_art"]:
            img = state.current_packet["album_art"].resize((250, 250), Image.LANCZOS)
        elif mainImage_orig:
            img = mainImage_orig.resize((250, 250), Image.LANCZOS)
        else:
            return
        photo = ImageTk.PhotoImage(img)
        album_label_widget.config(image=photo)
        album_label_widget.image = photo  # keep reference!


def play():
    if not state.playlist:
        # Try loading from music/ folder first
        from app.packet import load_songs_from_folder
        load_songs_from_folder()
        if state.playlist:
            load_and_play(0)
        return

    # Never started → start it
    if not pygame.mixer.music.get_busy() and not state.is_playing:
        load_and_play(state.current_index)
        return

    # Playing → pause
    if state.is_playing:
        pygame.mixer.music.pause()
        state.is_playing = False
    # Paused → resume
    else:
        pygame.mixer.music.unpause()
        state.is_playing = True


def next_song():
    if not state.playlist:
        return
    idx = random.randint(0, len(state.playlist) - 1) if state.is_shuffled else state.current_index + 1
    load_and_play(idx % len(state.playlist))


def prev_song():
    if not state.playlist:
        return
    load_and_play((state.current_index - 1) % len(state.playlist))