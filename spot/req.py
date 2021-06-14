import requests

tok = "BQC0Em5PZNWQmtNQxa49mPJ9EE6erC4RLjhmj94EW2Ta948xdxhmRrReOjVlg9jXMOLjRsGswDMTRSRr6IVyXmTt6uqbcR0OoSKGRWpLpvdIlFT3-WjeZnsv2Tk3Whv9ic-NU8GgQzuHnNigjVUGmupznA-4dJIlXvWacrcGiC9BlfX-Q_eon1JirMnyNmfS"


def get_id(track_name, token: str) -> str:
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer ' + token,
    }
    params = [
        ('q', track_name),
        ('type', 'track'),
    ]
    try:
        response = requests.get('https://api.spotify.com/v1/search',
                                headers=headers, params=params, timeout=5)
        json = response.json()
        first_result = json['tracks']['items'][0]
        track_id = first_result['id']
        return track_id
    except Exception:
        return ''


res = get_id('All Of Me (feat. Oliver Nelson)', tok)

print(res)
