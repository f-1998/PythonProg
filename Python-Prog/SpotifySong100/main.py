from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

year = input("Enter the year : ")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{Year}-08-12/")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")


# Set up your Spotify API credentials
SPOTIFY_CLIENT_ID = #Your spotify Client ID,
SPOTIFY_CLIENT_SECRET = #Your Spotify Client Secret
SPOTIFY_REDIRECT_URI = "http://example.com" #Your Spotify redirect uri


songs_name = soup.select(selector="li h3", class_="c-title")
songs_list = []

for song in songs_name:
    text = song.getText().strip()
    songs_list.append(text)




# Set up Spotipy with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                               client_secret=SPOTIFY_CLIENT_SECRET,
                                               redirect_uri=SPOTIFY_REDIRECT_URI,
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               scope='playlist-modify-private'))



user = sp.current_user()

# Create a new playlist
playlist_name = 'Billboard to Spotify'
user_id = #Your Spotify user ID from the Spotify app or API
playlist = sp.user_playlist_create(user_id, playlist_name, public=False)



for name in songs_list:
    result = sp.search(f"track:{name} year:{Year}", type="track")
    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        track_uris = [song_uri]
        sp.playlist_add_items(playlist['id'], track_uris)
    except IndexError:
        print(f"{name} is not on Spotify.")
        pass
