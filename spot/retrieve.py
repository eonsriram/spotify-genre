import json
from spotipy import Spotify
from spotipyutils import getToken, getGenre, storeJson


sp = Spotify(auth=getToken())


with open("results2.json", 'r') as file:
    resdict = json.load(file)

'''
for track in range(50):
    print(resdict["items"][track]["track"]["album"]["name"])
    #print(res["items"][track]["track"]["id"])
    #print(res["items"][track]["track"]["album"]["artists"][0]["name"])
'''

dict1 = {}

ctr = 0
for item in range(50):
    print('.',end=' ')
    id = resdict["items"][item]["track"]["id"]
    #print(id)
    name = resdict["items"][item]["track"]["album"]["name"]

    feat = sp.audio_features([id])[0]
    feat.pop('track_href')
    feat.pop('analysis_url')
    feat.pop('type')
    feat.pop('id')
    feat.pop('uri')


    dict1[item] = {'name': name, 'genre': getGenre(id), **feat}


print(dict1)
print()

dict2 = {'Name': [dict1[x]['name'] for x in range(50)],
         'genre': [dict1[x]['genre'] for x in range(50)],
         'danceability': [dict1[x]['danceability'] for x in range(50)],
         'energy': [dict1[x]['energy'] for x in range(50)],
         'loudness': [dict1[x]['loudness'] for x in range(50)],
         'mode': [dict1[x]['mode'] for x in range(50)],
         'speechiness': [dict1[x]['speechiness'] for x in range(50)],
         'acousticness': [dict1[x]['acousticness'] for x in range(50)],
         'instrumentalness': [dict1[x]['instrumentalness'] for x in range(50)],
         'liveness': [dict1[x]['liveness'] for x in range(50)],
         'valence': [dict1[x]['valence'] for x in range(50)],
         'tempo': [dict1[x]['tempo'] for x in range(50)],
         'duration_ms': [dict1[x]['duration_ms'] for x in range(50)],
         'time_signature': [dict1[x]['time_signature'] for x in range(50)]
         }

print(dict2)

storeJson(dict2, "Dataframe2.json")

