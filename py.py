# shows a user's playlists (need to be authenticated via oauth)

import sys
import spotipy
import spotipy.util as util
import json
from random_words import RandomWords


class Track():
    def __init__(self, name, artists, image, ):
        self.name = name
        self.artists = artists
        self.image = image


def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" %
              (i, track['artists'][0]['name'], track['name']))

all_tracks = []
username = 'quartz77'
playlist_id = '38Zfyh1nPszegqBO6JdtDe'
track_ids = ['4KKzv6Ml2tV5ueRMNrEDK3']  # tracks to be added

token = util.prompt_for_user_token(username,
                                   'playlist-modify-private',
                                   'eead53655c004b5fbe93be6c4fa33089',
                                   'fecfc626412b4f0d9d8977d53d7cdbf5',
                                   'http://localhost/')


def get_data(username, playlist_id):
    if token:
        sp = spotipy.Spotify(auth=token)
        playlist = sp.user_playlist(username, playlist_id)

        track_count = len(playlist['tracks']['items'])
        for t in range(track_count):
            track = {}
            artists = ""

            info = playlist['tracks']['items'][t]['track']
            track_id = info['uri'].split(':')[2]
            image = info['album']['images'][0][
                'url']  # put a loop here if neessary
            name = info['name']

            for a in range(len(info['album']['artists'])):
                if a > 0:
                    artists = artists + ', ' + \
                        info['album']['artists'][a]['name']
                else:
                    artists = info['album']['artists'][a]['name']
            print(track_id)
            all_tracks.append(Track(name, artists, image))
    else:
        print("Can't get token for", username)


def add_track(id):
    if token:
        rw = RandomWords()
        word = rw.random_word()

        sp = spotipy.Spotify(auth=token)
        new_song = sp.search(word, limit=1)
        playlist = sp.user_playlist(username, playlist_id)
        sp.trace = False
        results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    else:
        print("Can't get token for", username)

def remove_track(id):
	if token:
		playlist = sp.user_playlist(username, playlist_id)
		results = sp.results = sp.user_playlist_remove_specific_occurrences_of_tracks(username, playlist_id, track_ids)

	else:
		print("Can't get token for", username)

def remove_all_tracks():
	if token:
		results = sp.user_playlist_remove_all_occurrences_of_tracks(username, playlist_id, track_ids)

	else:
		print("Can't get token for", username)

get_data(username, playlist_id)
print(all_tracks[2].artists)
