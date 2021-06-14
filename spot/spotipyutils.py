import spotipy.util as util
from spotipy import SpotifyClientCredentials, Spotify, SpotifyOAuth
import os
import json


def getToken():
    username = 'erigonox'
    client_id = 'df2dfb8e80be4938abea615253dd367b'
    client_secret = '82465aafe1d44b5dace58b0a6adfbbe3'
    redirect_uri = 'http://localhost:7777/callback'
    scope = 'user-library-read'

    token = util.prompt_for_user_token(username=username,
                                       scope=scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    return token


# tok = getToken()
# sp = Spotify(auth=tok)

# res = sp.search("Avicii", type="artist", limit=1)
# print(res)

def getGenre(id):
    tok = getToken()
    sp = Spotify(auth=tok)

    tr = sp.track(id)
    art_id = tr["album"]["artists"][0]["id"]
    genres = sp.artist(art_id)["genres"]
    if len(genres) >= 1:
        return genres[0]
    else:
        return ''


def storeJson(resdict, out_file_name):
    if os.path.exists(out_file_name):
        os.remove(out_file_name)
    with open(out_file_name, "w") as outfile:
        json.dump(resdict, outfile, indent=2)


def readJson(file_name):
    with open(file_name, 'r') as file:
        res = json.load(file)
        return res



if __name__ == '__main__':
    print(getToken())
