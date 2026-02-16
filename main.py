import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Music Player")
root.geometry("420x600")
root.config(bg="#1a1a1a")  # Dark background

# --- Load images ---
searchImage = Image.open("C:/Users/bismiallah/Desktop/Projects/Music-Player-app/assets/search.jpg")
searchImage = searchImage.resize((25, 25))
search = ImageTk.PhotoImage(searchImage)

mainImage = Image.open("C:/Users/bismiallah/Desktop/Projects/Music-Player-app/assets/note.jpg")
mainImage = mainImage.resize((250, 250))
photo = ImageTk.PhotoImage(mainImage)

playImage = Image.open("C:/Users/bismiallah/Desktop/Projects/Music-Player-app/assets/play.jpg").resize((60, 60))
play = ImageTk.PhotoImage(playImage)

nextImage = Image.open("C:/Users/bismiallah/Desktop/Projects/Music-Player-app/assets/right arrow.jpg").resize((50, 50))
next_btn = ImageTk.PhotoImage(nextImage)

previousImage = Image.open("C:/Users/bismiallah/Desktop/Projects/Music-Player-app/assets/left arrow.jpg").resize((50, 50))
previous_btn = ImageTk.PhotoImage(previousImage)

# --- Top bar with search ---
top_frame = tk.Frame(root, bg="#1a1a1a", height=60)
top_frame.pack(fill="x", padx=10, pady=10)

search_button = tk.Button(top_frame, image=search, bd=0, bg="#1a1a1a", 
                          activebackground="#2a2a2a", cursor="hand2")
search_button.pack(side="right")

# Spacer to push album to center
spacer = tk.Frame(root, bg="#1a1a1a", height=30)
spacer.pack()

# --- Album art in center ---
album_label = tk.Label(root, image=photo, bg="#1a1a1a")
album_label.pack(pady=20)

# --- Song info ---
song_title = tk.Label(root, text="Song Title", font=("Arial", 16, "bold"), 
                      bg="#1a1a1a", fg="white")
song_title.pack(pady=5)

artist_name = tk.Label(root, text="Artist Name", font=("Arial", 12), 
                       bg="#1a1a1a", fg="#888888")
artist_name.pack(pady=5)

# --- Progress bar ---
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

time_end = tk.Label(progress_frame, text="3:45", font=("Arial", 9), 
                    bg="#1a1a1a", fg="#888888")
time_end.pack(side="right")

# --- Control buttons ---
buttons_frame = tk.Frame(root, bg="#1a1a1a")
buttons_frame.pack(pady=20)

previous = tk.Button(buttons_frame, image=previous_btn, bd=0, bg="#1a1a1a",
                     activebackground="#2a2a2a", cursor="hand2",
                     command=lambda: print("Previous"))
previous.pack(side="left", padx=15)

play_button = tk.Button(buttons_frame, image=play, bd=0, bg="#1a1a1a",
                        activebackground="#2a2a2a", cursor="hand2",
                        command=lambda: print("Play"))
play_button.pack(side="left", padx=15)

next_button = tk.Button(buttons_frame, image=next_btn, bd=0, bg="#1a1a1a",
                        activebackground="#2a2a2a", cursor="hand2",
                        command=lambda: print("Next"))
next_button.pack(side="left", padx=15)

# --- Volume control (optional) ---
volume_frame = tk.Frame(root, bg="#1a1a1a")
volume_frame.pack(pady=10)

volume_label = tk.Label(volume_frame, text="🔊", font=("Arial", 14), 
                        bg="#1a1a1a", fg="white")
volume_label.pack(side="left", padx=5)

volume_slider = tk.Scale(volume_frame, from_=0, to=100, orient="horizontal",
                         length=150, bg="#1a1a1a", fg="white", 
                         troughcolor="#333333", highlightthickness=0, 
                         bd=0, showvalue=0, activebackground="#1DB954")
volume_slider.set(70)
volume_slider.pack(side="left")

root.mainloop()