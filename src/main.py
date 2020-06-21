from tag_to_playlist import tag_to_playlist as lib
import config

def main ():

    
    spotlib = lib(config)
    lastfm_connection = spotlib.connect_to_lastfm()
    if lastfm_connection:
        print("Connected to lastfm!")
    else:
        print("Connection to lastfm failed!")

    
    """
    spotify_connection = spotlib.connect_to_spotify()
    if spotify_connection:
        print("Connected")
    else:
        print("Spotify connection fails")
    
    """
  


if __name__ == "__main__":
    main()

