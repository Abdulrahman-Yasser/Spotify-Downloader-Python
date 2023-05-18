import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from pytube import Search
from pytube import YouTube

class mySpotifyDownloader:
    def __init__(self, URLs, SAVE_FILE):
        self.broken_URL = []
        self.broken_titles = []
        self.my_URLs = URLs
        self.OldLength = 0
        self.OldDate = 0
        self.SAVE_FILE = SAVE_FILE

    def check(self):
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        p = sp.playlist_tracks(self.my_URLs,fields='items.track.name, items.track.artists.name, total, items.added_at' )
        try:
            new_OldDate = p['items'][-1]['added_at']
        except ValueError:
            print(p.length)
            new_OldDate = 1
        if new_OldDate == self.OldDate:
            return False
        else:
            return True


    def download(self):
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        ListOfNewSongs = []
        TupleOfNewSongsArtist =  dict()
        p = sp.playlist_tracks(self.my_URLs,fields='items.track.name, items.track.artists.name, total, items.added_at' )
        newOldDate = p['items'][-1]['added_at']
        if newOldDate != self.OldDate:
            newLength = p['total']
            for songs in p['items'][self.OldLength : newLength]:
                ListOfNewSongs.append(songs['track']['name'])
                TupleOfNewSongsArtist.update({songs['track']['name']:songs['track']['artists']})
            self.OldLength = newLength
            self.OldDate = newOldDate
        for song in ListOfNewSongs:
            my_artist = ""
            for art in TupleOfNewSongsArtist[song]:
                my_artist = my_artist + " " + str(art['name'])
            try:
                print("Going to download " + song + " " + my_artist)
            except:
                print("Arabic")
            q = Search(song + " " + my_artist)
            try:
                temper = 0
                while(q.results[temper].length > 600):
                    temper = temper + 1
                    if(temper > 17):
                        self.broken_titles.append(q.results[0].title)
                        break
                if temper > 17:
                    continue
                aud = q.results[0].streams.filter(only_audio=True).last().download(self.SAVE_FILE)
            except:
                self.broken_URL.append(q.results[0].watch_url)
                print("Some error")


    def showAllBroken(self):
        self.showAllBrokenUrl()
        self.showAllBrokenTitles()


    def showAllBrokenUrl(self):
        for i in self.broken_URL:
            print(i)


    def showAllBrokenTitles(self):
        for i in self.broken_titles:
            print(i)


    def download_brokenUrl(self):
        for i in self.broken_URL:
            y = YouTube(i)
            try:
                y.streams.filter(only_audio=True).last().download(self.SAVE_FILE)
                self.broken_URL.clear(i)
            except:
                print("Still not fixed",i)

    def showAllSongs(self):
        sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        ListOfNewSongs = []
        TupleOfNewSongsArtist =  dict()
        p = sp.playlist_tracks(self.my_URLs,fields='items.track.name, items.track.artists.name, total, items.added_at' )
        for songs in p['items'][0:]:
            ListOfNewSongs.append(songs['track']['name'])
            TupleOfNewSongsArtist.update({songs['track']['name']:songs['track']['artists']})
        for song in ListOfNewSongs:
            my_artist = ""
            for art in TupleOfNewSongsArtist[song]:
                my_artist = my_artist + " " + str(art['name'])
            try:
                print(song + " " + my_artist)
            except:
                print("arabic")



