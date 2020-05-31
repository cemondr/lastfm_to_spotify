import spotipy
import pylast
import config

class tag_to_playlist:

    def __init__(self):
        self.lastfm_api_key = config.lastfm_api_key
        self.lastfm_api_secret = config.lastfm_api_secret
        self.lastfm_username = config.lastfm_username
        self.lastfm_password = pylast.md5(config.lastfm_password)

    def connect_to_lastfm(self):
        self.lastfm_network = pylast.LastFMNetwork(api_key=self.lastfm_api_key,api_secret=self.lastfm_api_secret,username=self.lastfm_username,password_hash=self.lastfm_password)

    def get_tagged_songs(self,tag_name):
        return self.lastfm_network.get_tag(tag_name)

    def get_songs_from_tag(self,tag):
        return tag.get_top_tracks()

    def connect_to_spotify(self):
        pass
    
    def is_playlist_there(self,tag):
        pass

    def create_playlist(self):
        pass

    def add_to_playlist(self):
        pass

