import json
import spotipy
import webbrowser
from login_authentification import login_uzer

#Login into Spotify
spotify = login_uzer()

username = spotify.current_user()['id']
