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
playlist_POV_1937_url = {'name':'playlist_POV_1937_url','url':'https://open.spotify.com/playlist/1iakWdd8XdEhBG74T6ljoF?si=e891323577b54d50'}
playlist_ak46_url = {'name':'playlist_ak46_url','url':'https://open.spotify.com/playlist/65f9D4Nq9xFXdOs2ujk6dg?si=0fa873d18b274792'}
playlist_chaam_url = {'name':'playlist_chaam_url','url':'https://open.spotify.com/playlist/2OFL9hOLES9GeekhXjxC6M?si=8ba625d57f614720'}
playlist_myPrivate_url = {'name':'playlist_myPrivate_url','url':'https://open.spotify.com/playlist/7wsNApG0r9VxDfiTiSo56h?si=10686f0d9a1149fd'}

playlist_3asal_url = {'name':'playlist_3asal_url','url':'https://open.spotify.com/playlist/20lXmkSIwpu2hoyTRPUnzd?si=2ff86dac1ee74364'}
playlist_hotel_palestine = {'name':'playlist_chaaaam_url','url':'https://open.spotify.com/playlist/7MQkb1juFlr5XuGC0sMkEl?si=492cd0daff05495e'}
playlist_3atma_url = {'name':'playlist_3atma_url','url':'https://open.spotify.com/playlist/7hZ3lxki3i13Te7PzcJnfi?si=4e76d11406b348e8'}

all_my_Playlists = [playlist_3asal_url, playlist_hotel_palestine, playlist_3atma_url, playlist_myPrivate_url ]

from my_SpotifyDownloader.mySpotify_Downloader import mySpotifyDownloader


if __name__ == '__main__':

    sp_handler = []

#   just a place holder, i will load it's saved values from a pickle file via all_my_Playlists[i]['name']
    for i in range(len(all_my_Playlists)):
        sp_handler.append(mySpotifyDownloader(all_my_Playlists[i]['url'], SAVE_FILE))


    for i in range(len(all_my_Playlists)):
        try:
            with open(all_my_Playlists[i]['name']+'.pickle', 'rb') as file:
                sp_handler[i] :  mySpotifyDownloader = pickle.load(file)
        except:
            with open(all_my_Playlists[i]['name']+'.pickle', 'wb') as file:
                pickle.dump(sp_handler[i], file)


    for sp in sp_handler:
        sp.download()

    for i in range(len(all_my_Playlists)):
        with open(all_my_Playlists[i]['name']+'.pickle', 'wb') as file:
            pickle.dump(sp_handler[i], file)
