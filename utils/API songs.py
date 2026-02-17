import requests
import pygame

pygame.mixer.init()

song = "eminem"

url = f"https://api.deezer.com/search?q={song}"
data = requests.get(url).json()

preview_url = data["data"][0]["preview"]

# download preview
audio = requests.get(preview_url).content
with open("song.mp3","wb") as f:
    f.write(audio)

pygame.mixer.music.load("song.mp3")
pygame.mixer.music.play()
