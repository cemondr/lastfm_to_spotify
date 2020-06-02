import spotipy
import pylast
import config

class tag_to_playlist:

    DESCRIPTION = "Imported from last.fm tag"

    def __init__(self):
        self.lastfm_api_key = config.lastfm_api_key
        self.lastfm_api_secret = config.lastfm_api_secret
        self.lastfm_username = config.lastfm_username
        self.lastfm_password = pylast.md5(config.lastfm_password)
        self.spotify_username = config.spotify_username
        self.spotify_password = config.spotify_password
        self.spotify_api_key = config.spotify_api_key
        self.spotify_api_secret = config.spotify_api_secret
        self.spotify_redirect_uri = config.spotify_redirect_uri

    def connect_to_lastfm(self):
        self.lastfm_network = pylast.LastFMNetwork(api_key=self.lastfm_api_key,api_secret=self.lastfm_api_secret,username=self.lastfm_username,password_hash=self.lastfm_password)

    def get_tagged_songs(self,tag_name):
        tag_content = lastfm_network.get_tag(tag_name)
        return tag_content.get_top_tracks()

    def connect_to_spotify(self):
        self.spotify_token = spotipy.prompt_for_user_token(username=self.spotify_username,scope="playlist-modify-public playlist-modify-private",client_id=self.spotify_api_key,client_secret=self.spotify_api_secret,redirect_uri=self.spotify_redirect_uri)
    
    def is_playlist_there(self,tag):
        pass

    def create_playlist(self):
        pass

    def add_to_playlist(self):
        pass

