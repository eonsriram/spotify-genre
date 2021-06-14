from spotipy import SpotifyClientCredentials, Spotify, SpotifyOAuth
import json
import os
from spotipyutils import getToken, getGenre, storeJson, readJson


#tok = "BQC0Em5PZNWQmtNQxa49mPJ9EE6erC4RLjhmj94EW2Ta948xdxhmRrReOjVlg9jXMOLjRsGswDMTRSRr6IVyXmTt6uqbcR0OoSKGRWpLpvdIlFT3-WjeZnsv2Tk3Whv9ic-NU8GgQzuHnNigjVUGmupznA-4dJIlXvWacrcGiC9BlfX-Q_eon1JirMnyNmfS"

tok = getToken()
'''
username = 'erigonox'
client_id = 'df2dfb8e80be4938abea615253dd367b'
client_secret = '82465aafe1d44b5dace58b0a6adfbbe3'
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-library-read'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
auth = SpotifyOAuth(client_id=client_id,
                    client_secret=client_secret,
                    redirect_uri=redirect_uri,
                    username=username,
                    scope=scope)

sp = Spotify(client_credentials_manager=client_credentials_manager, auth_manager=auth)

'''


sp = Spotify(auth=tok)

resdict = sp.current_user_saved_tracks(limit=50, offset=0)
storeJson(resdict, "results1.json")
resdict = sp.current_user_saved_tracks(limit=50, offset=51)
storeJson(resdict, "results2.json")

# ________________________________________________

res = readJson("results2.json")


id = res["items"][14]["track"]["id"]
print(tok)
print(id)
print(res["items"][14]["track"]["album"]["name"])

feat = sp.audio_features([id])

print(feat)
print(getGenre(id))
