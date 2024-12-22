"""This module is dedicated to provide login credentials of the user for Spotify"""

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def login_uzer():
    """retrieves the username inputted from the user on Spotify"""
    user_input = input("Enter Username:\t") #prompt username from the user
    clientID = os.environ.get("SPOTIPY_CLIENT_ID")
    clientSecret = os.environ.get("SPOTIPY_CLIENT_SECRET")
    redirect_uri = 'http://google.com/callback/'

    oauth_object = spotipy.SpotifyOAuth(username=user_input,client_id=clientID, client_secret=clientSecret, redirect_uri=redirect_uri)
    token_dict = oauth_object.get_cached_token()     #Validate user input
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)    # #Spotify usernames do not accept spaces
    # spotifyObject = spotipy.Spotify(auth=spotipy.SpotifyOAuth(client_id=clientID,
    #                                                   client_secret=clientSecret,
    #                                                   redirect_uri=redirect_uri))    
    user_name = spotifyObject.current_user()['id']

    # while len(user_input.split()) > 1:
    #     #Display error 
    #     user_input = input("Enter Username:\t")

    return spotifyObject
