import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# Define the Spotify playlist URL
playlist_url = "https://open.spotify.com/playlist/44kgWZRt5jmmgppH0qGszg"

playlist_id = playlist_url.split("/")[-1]
results = sp.playlist_tracks(playlist_id)

results