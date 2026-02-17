import pygame

# ─────────────────────────────────────────────
#  PATHS
# ─────────────────────────────────────────────
ASSETS    = "assets"
MUSIC_DIR = "music"

# ─────────────────────────────────────────────
#  PLAYBACK STATE
# ─────────────────────────────────────────────
playlist       = []
current_index  = 0
current_packet = {}
is_playing     = False
is_shuffled    = False
is_looping     = False
seeking        = False
total_duration = 0
query          = ""