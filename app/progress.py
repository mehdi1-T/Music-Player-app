import pygame
import app.state as state
from app.playback import load_and_play, next_song, fmt_time

# ui references — set by ui.py
progress_bar_widget = None
time_start_widget   = None
root_widget         = None


def update_progress():
    if state.is_playing and pygame.mixer.music.get_busy():
        pos_ms = pygame.mixer.music.get_pos()
        if pos_ms >= 0 and not state.seeking:
            pos_sec = pos_ms / 1000
            if progress_bar_widget:
                progress_bar_widget.set(pos_sec)
            if time_start_widget:
                time_start_widget.config(text=fmt_time(pos_sec))

    # Auto-advance when song ends
    if state.is_playing and not pygame.mixer.music.get_busy():
        if state.is_looping:
            load_and_play(state.current_index)
        else:
            next_song()

    if root_widget:
        root_widget.after(500, update_progress)


def on_seek_start(event):
    state.seeking = True


def on_seek_end(event):
    state.seeking = False
    if progress_bar_widget:
        pos = progress_bar_widget.get()
        pygame.mixer.music.set_pos(pos)
        if time_start_widget:
            time_start_widget.config(text=fmt_time(pos))