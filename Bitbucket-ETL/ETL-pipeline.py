import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd



client_credentials_manager = SpotifyClientCredentials(client_id='7b5265fcb1ca4c3aa1f8ce857efb3fcf', client_secret='1b576248579747d5aed8c0ee3620b536')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Define the Spotify playlist URL
playlist_url = "https://open.spotify.com/playlist/44kgWZRt5jmmgppH0qGszg"

playlist_id = playlist_url.split("/")[-1]
results = sp.playlist_tracks(playlist_id)

results