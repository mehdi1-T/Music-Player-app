import requests

url = "https://api.spotify.com/v1/search"
headers = {"Authorization": "Bearer YOUR_TOKEN"}
params = {"q": "Imagine Dragons", "type": "track"}

r = requests.get(url, headers=headers, params=params)
print(r.json())


"""
Search bar → API request → results list
                      ↓
               select song
                      ↓
            play local or preview audio

"""