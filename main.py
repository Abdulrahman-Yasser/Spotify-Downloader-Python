import pickle
import os


my_export_variables = 'D:/_Study_A/PrivateFiles/commands.txt'

f = open(my_export_variables, "r")
SPOTIPY_CLIENT_ID = f.readlines()[0]
i = SPOTIPY_CLIENT_ID.index("'")
SPOTIPY_CLIENT_ID = str(SPOTIPY_CLIENT_ID[i+1:-2])
print(SPOTIPY_CLIENT_ID)

f = open(my_export_variables, "r")
SPOTIPY_CLIENT_SECRET  = f.readlines()[1]
i = SPOTIPY_CLIENT_SECRET .index("'")
SPOTIPY_CLIENT_SECRET  = str(SPOTIPY_CLIENT_SECRET[i+1:-2])
print(SPOTIPY_CLIENT_SECRET)

f = open(my_export_variables, "r")
SPOTIPY_REDIRECT_URL  = f.readlines()[2]
i = SPOTIPY_REDIRECT_URL .index("'")
SPOTIPY_REDIRECT_URL  = str(SPOTIPY_REDIRECT_URL[i+1:-2])
print(SPOTIPY_REDIRECT_URL)

os.environ['SPOTIPY_CLIENT_ID'] = SPOTIPY_CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = SPOTIPY_CLIENT_SECRET
os.environ['SPOTIPY_REDIRECT_URL'] = SPOTIPY_REDIRECT_URL


SAVE_FILE = "D:\_Study_A\my_refresh_music"
playlist_POV_1937_url = 'https://open.spotify.com/playlist/1iakWdd8XdEhBG74T6ljoF?si=e891323577b54d50'
playlist_ak46_url = 'https://open.spotify.com/playlist/65f9D4Nq9xFXdOs2ujk6dg?si=0fa873d18b274792'
playlist_chaam_url = 'https://open.spotify.com/playlist/2OFL9hOLES9GeekhXjxC6M?si=8ba625d57f614720'
playlist_myPrivate_url = 'https://open.spotify.com/playlist/5eFGpc0IFHXQ2LKEYzGpG0?si=637324a2a68b4725'

from my_SpotifyDownloader.mySpotify_Downloader import mySpotifyDownloader

if __name__ == '__main__':



    # sp_handler_1973 = mySpotifyDownloader(playlist_POV_1937_url, SAVE_FILE)
    # sp_handler_ak47 = mySpotifyDownloader(playlist_ak46_url, SAVE_FILE)
    # sp_handler_chaam = mySpotifyDownloader(playlist_chaam_url, SAVE_FILE)
    sp_handler_prv = mySpotifyDownloader(playlist_myPrivate_url, SAVE_FILE)



    # with open('1973.pickle', 'rb') as file:
    #     sp_handler_1973 : mySpotifyDownloader = pickle.load(file)
    # with open('ak47.pickle', 'rb') as file:
    #     sp_handler_ak47 : mySpotifyDownloader = pickle.load(file)
    # with open('chaam.pickle', 'rb') as file:
    #     sp_handler_chaam : mySpotifyDownloader = pickle.load(file)
    with open('prv.pickle', 'rb') as file:
        sp_handler_prv : mySpotifyDownloader = pickle.load(file)


    # sp_handler_1973.download()
    # sp_handler_ak47.download()
    # sp_handler_chaam.download()
    sp_handler_prv.download()

    # with open('1973.pickle', 'rb') as file:
    #     pickle.dump(sp_handler_1973, file)
    # with open('ak47.pickle', 'rb') as file:
    #     pickle.dump(sp_handler_ak47, file)
    # with open('chaam.pickle', 'rb') as file:
    #     pickle.dump(sp_handler_chaam, file)
    with open('prv.pickle', 'wb') as file:
        pickle.dump(sp_handler_prv, file)
