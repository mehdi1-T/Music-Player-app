import os
import pygame
from tkinter import filedialog
import app.state as state
from app.playback import load_and_play

# ui reference — set by ui.py
search_input_widget = None


def skip_forward_10():
    if not state.playlist:
        return
    pos = pygame.mixer.music.get_pos() / 1000 + 10
    pos = min(pos, state.total_duration)
    pygame.mixer.music.set_pos(pos)
    from app.playback import progress_bar_widget
    if progress_bar_widget:
        progress_bar_widget.set(int(pos))


def skip_backward_10():
    if not state.playlist:
        return
    pos = pygame.mixer.music.get_pos() / 1000 - 10
    pos = max(pos, 0)
    pygame.mixer.music.set_pos(pos)
    from app.playback import progress_bar_widget
    if progress_bar_widget:
        progress_bar_widget.set(int(pos))


def search():
    if not search_input_widget:
        return

    state.query = search_input_widget.get().strip()

    # Direct file path typed in search bar
    if os.path.isfile(state.query):
        if state.query not in state.playlist:
            state.playlist.append(state.query)
        load_and_play(state.playlist.index(state.query))
        return

    # Search by filename inside the playlist
    for i, path in enumerate(state.playlist):
        if state.query.lower() in os.path.basename(path).lower():
            load_and_play(i)
            return


def add_files():
    files = filedialog.askopenfilenames(
        title="Add songs",
        filetypes=[("Audio files", "*.mp3 *.wav *.ogg *.flac"), ("All files", "*.*")]
    )
    for f in files:
        if f not in state.playlist:
            state.playlist.append(f)
    if state.playlist:
        load_and_play(0)