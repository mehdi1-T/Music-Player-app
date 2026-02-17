import tkinter as tk
import pygame

pygame.init()
pygame.mixer.init()

from app.ui import build_ui
from app.packet import load_songs_from_folder
from app.progress import update_progress

root = tk.Tk()

build_ui(root)              # build all widgets
load_songs_from_folder()    # load music/ folder into playlist
update_progress()           # start progress loop

root.mainloop()