def search():
    global query
    query = search_input.get()
    play_song(query)