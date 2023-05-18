import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from pytube import YouTube
from pytube import Search

playlist_POV_1937 = 'https://open.spotify.com/playlist/1iakWdd8XdEhBG74T6ljoF?si=e891323577b54d50'
playlist_ak46 = 'https://open.spotify.com/playlist/65f9D4Nq9xFXdOs2ujk6dg?si=0fa873d18b274792'
playlist_chaam = 'https://open.spotify.com/playlist/2OFL9hOLES9GeekhXjxC6M?si=8ba625d57f614720'
my_playlists = [playlist_POV_1937, playlist_ak46, playlist_chaam]

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


from pprint import pprint

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

pl_id = 'https://open.spotify.com/playlist/5eFGpc0IFHXQ2LKEYzGpG0?si=6ab8c61d78774e01'
SAVE_FILE = "D:\_Study_A\my_refresh_music"

p = sp.playlist_tracks(pl_id,fields='items.track.name, items.track.artists.name, total, items.added_at' )
print(p)
ListOfNewSongs = []
broken_url = []
broken_titles = []
TupleOfNewSongsArtist = dict()
print(p['items'][-1]['added_at'])
for songs in p['items'][0:]:
    ListOfNewSongs.append(songs['track']['name'])
    TupleOfNewSongsArtist.update({songs['track']['name']:songs['track']['artists']})

my_artist = ""
print(ListOfNewSongs)
print(TupleOfNewSongsArtist)
for song in ListOfNewSongs:
    my_artist = ""
    for art in TupleOfNewSongsArtist[song]:
        my_artist = my_artist + " " + str(art['name'])
    print(song + " " + my_artist)
    q = Search(song + " " + my_artist)
    print(len(q.results))
    print(q.results[0])
    try:
        temper = 0
        while(q.results[temper].length > 600):
            temper = temper + 1
            if(temper > 17):
                broken_titles.append(q.results[0].title)
                break
        if temper > 17:
            continue
        aud = q.results[0].streams.filter(only_audio=True).last().download(SAVE_FILE)
    except:
        broken_url.append(q.results[0].watch_url)
        print("Some error")
   