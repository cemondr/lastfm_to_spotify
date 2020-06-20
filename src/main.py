from tag_to_playlist import tag_to_playlist as lib
import config

def main ():

    spotlib = lib(config)
    spotify_connection = spotlib.connect_to_spotify()
    if spotify_connection:
        print("Connected")
    else:
        print("Spotify connection fails")
  


if __name__ == "__main__":
    main()

