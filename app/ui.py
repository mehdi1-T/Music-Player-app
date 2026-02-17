import tkinter as tk
from PIL import Image, ImageTk
import app.state as state
import app.playback as playback
import app.progress as progress
import app.controls as controls
from app.controls import search, add_files, skip_forward_10, skip_backward_10
from app.playback import play, next_song, prev_song


def build_ui(root):
    root.title("Music Player")
    root.geometry("420x640")
    root.config(bg="#1a1a1a")

    # ── Load asset images ─────────────────────
    ASSETS = state.ASSETS

    logoImage = Image.open(f"{ASSETS}/logo-spotify.jpg")
    logo      = ImageTk.PhotoImage(logoImage)
    root.iconphoto(True, logo)

    searchImage = Image.open(f"{ASSETS}/search.jpg").resize((25, 25))
    search_icon = ImageTk.PhotoImage(searchImage)

    mainImage_orig = Image.open(f"{ASSETS}/note.jpg")
    mainImage_disp = mainImage_orig.resize((250, 250))
    photo          = ImageTk.PhotoImage(mainImage_disp)

    playImage = Image.open(f"{ASSETS}/play.jpg").resize((60, 60))
    play_icon = ImageTk.PhotoImage(playImage)

    nextImage = Image.open(f"{ASSETS}/right arrow.jpg").resize((50, 50))
    next_icon = ImageTk.PhotoImage(nextImage)

    previousImage = Image.open(f"{ASSETS}/left arrow.jpg").resize((50, 50))
    prev_icon     = ImageTk.PhotoImage(previousImage)

    # Share mainImage_orig with playback so fallback art works
    playback.mainImage_orig = mainImage_orig

    # ── TOP BAR ───────────────────────────────
    top_frame = tk.Frame(root, bg="#1a1a1a", height=60)
    top_frame.pack(fill="x", padx=10, pady=10)

    search_button = tk.Button(top_frame, image=search_icon, bd=0, bg="#1a1a1a",
                              activebackground="#2a2a2a", cursor="hand2", command=search)
    search_button.pack(side="right")
    search_button.image = search_icon  # keep reference

    add_btn = tk.Button(top_frame, text="＋", font=("Arial", 14, "bold"),
                        fg="#1DB954", bg="#1a1a1a", bd=0,
                        activebackground="#2a2a2a", cursor="hand2",
                        command=add_files)
    add_btn.pack(side="right", padx=6)

    search_input = tk.Entry(top_frame, width=80)
    search_input.pack(side="left", padx=100, pady=20)

    # Wire search input to controls
    controls.search_input_widget = search_input

    # ── SPACER ────────────────────────────────
    tk.Frame(root, bg="#1a1a1a", height=30).pack()

    # ── ALBUM ART ─────────────────────────────
    album_label = tk.Label(root, image=photo, bg="#1a1a1a")
    album_label.pack(pady=10)
    album_label.image = photo  # keep reference

    # ── SONG INFO ─────────────────────────────
    song_title = tk.Label(root, text="No song loaded", font=("Arial", 16, "bold"),
                          bg="#1a1a1a", fg="white")
    song_title.pack(pady=5)

    artist_name = tk.Label(root, text="Artist", font=("Arial", 12),
                           bg="#1a1a1a", fg="#888888")
    artist_name.pack(pady=5)

    # ── PROGRESS BAR ──────────────────────────
    progress_frame = tk.Frame(root, bg="#1a1a1a")
    progress_frame.pack(fill="x", padx=40, pady=20)

    time_start = tk.Label(progress_frame, text="0:00", font=("Arial", 9),
                          bg="#1a1a1a", fg="#888888")
    time_start.pack(side="left")

    progress_bar = tk.Scale(progress_frame, from_=0, to=100, orient="horizontal",
                            bg="#1a1a1a", fg="white", troughcolor="#333333",
                            highlightthickness=0, bd=0, showvalue=0,
                            activebackground="#1DB954", sliderrelief="flat")
    progress_bar.pack(side="left", fill="x", expand=True, padx=10)
    progress_bar.bind("<ButtonPress-1>",   progress.on_seek_start)
    progress_bar.bind("<ButtonRelease-1>", progress.on_seek_end)

    time_end = tk.Label(progress_frame, text="0:00", font=("Arial", 9),
                        bg="#1a1a1a", fg="#888888")
    time_end.pack(side="right")

    # ── CONTROL BUTTONS ───────────────────────
    buttons_frame = tk.Frame(root, bg="#1a1a1a")
    buttons_frame.pack(pady=20)

    tk.Button(buttons_frame, image=prev_icon, bd=0, bg="#1a1a1a",
              activebackground="#2a2a2a", cursor="hand2",
              command=skip_backward_10).pack(side="left", padx=15)

    tk.Button(buttons_frame, image=play_icon, bd=0, bg="#1a1a1a",
              activebackground="#2a2a2a", cursor="hand2",
              command=play).pack(side="left", padx=15)

    tk.Button(buttons_frame, image=next_icon, bd=0, bg="#1a1a1a",
              activebackground="#2a2a2a", cursor="hand2",
              command=skip_forward_10).pack(side="left", padx=15)

    # Keep button image references
    buttons_frame.prev_icon = prev_icon
    buttons_frame.play_icon = play_icon
    buttons_frame.next_icon = next_icon

    # ── Wire widgets to other modules ─────────
    playback.song_title_widget   = song_title
    playback.artist_name_widget  = artist_name
    playback.time_start_widget   = time_start
    playback.time_end_widget     = time_end
    playback.progress_bar_widget = progress_bar
    playback.album_label_widget  = album_label

    progress.progress_bar_widget = progress_bar
    progress.time_start_widget   = time_start
    progress.root_widget         = root

    # ── Keyboard shortcuts ────────────────────────

    root.bind("<space>", lambda event: play())
    search_input.bind("<Return>", lambda event: search())

    # ── Wire widgets to other modules ─────────
    playback.song_title_widget   = song_title
    playback.artist_name_widget  = artist_name
    playback.time_start_widget   = time_start
    playback.time_end_widget     = time_end
    playback.progress_bar_widget = progress_bar
    playback.album_label_widget  = album_label

    progress.progress_bar_widget = progress_bar
    progress.time_start_widget   = time_start
    progress.root_widget         = root

    # ── Keyboard shortcuts ────────────────────  ← ADD FROM HERE
    def on_space(event):
        if event.widget != search_input:
            play()

    root.bind("<space>", on_space)
    search_input.bind("<Return>", lambda event: search())
    # ─────────────────────────────────────────  ← TO HERE