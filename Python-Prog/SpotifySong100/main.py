from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


response = requests.get("https://www.billboard.com/charts/hot-100/2010-08-12/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")


# Set up your Spotify API credentials
SPOTIPY_CLIENT_ID = "ec2586d6d3a14260bd4b8cc9fa059c1e"
SPOTIPY_CLIENT_SECRET = "5b80a92616a84b9f9e7f8fcf7e893609"
SPOTIPY_REDIRECT_URI = "http://example.com"


songs_name = soup.select(selector="li h3", class_="c-title")
songs_list = []

for song in songs_name:
    text = song.getText().strip()
    songs_list.append(text)




# Set up Spotipy with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               scope='playlist-modify-private'))



user = sp.current_user()

# Create a new playlist
playlist_name = 'Billboard to Spotify'
user_id = '6eay7klir8xpd8x0aakh1kejo'  # You can get your Spotify user ID from the Spotify app or API
playlist = sp.user_playlist_create(user_id, playlist_name, public=False)



for name in songs_list:
    result = sp.search(f"track:{name} year:2010", type="track")
    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        track_uris = [song_uri]
        sp.playlist_add_items(playlist['id'], track_uris)
    except IndexError:
        print(f"{name} is not on Spotify.")
        pass
