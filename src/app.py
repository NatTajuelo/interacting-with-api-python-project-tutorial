import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy 
from spotipy.oauth2 import SpotifyClientCredentials


# load the .env file variables
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id = client_id, client_secret = client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

#artist = 'spotify:artist:64tJ2EAv1R6UaZqc4iOCyj'

artist = "64tJ2EAv1R6UaZqc4iOCyj"

result = sp.artist_top_tracks("64tJ2EAv1R6UaZqc4iOCyj")
if result: 
    tracks = result["tracks"] 
    tracks = [{k: (v/(1000*60))%60 if k == "duration_ms" else v 
    for k, v in track.items() if k in ["name", "popularity", "duration_ms"]} for track in tracks]
