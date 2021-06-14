from flask import Flask, render_template, request, redirect, url_for, session
import random
import string
from sql.sqlops import SQLDB
from spot.spotipyutils import getToken
from spotipy import Spotify

# db = SQLDB()
application = Flask(__name__)


def generator(size=7, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')


@application.route('/process', methods=['POST'])
def process():
    tok = getToken()
    return render_template('table.html')


@application.route('/callback', methods=['GET'])
def callback():
    auth_token = request.args['code']
    sp = Spotify(auth=auth_token)
    session['sp'] = sp
    tracks = sp.current_user_saved_tracks()
    return "Hello"


@application.route('/table')
@application.route(f'/{generator()}')
def table():
    db = SQLDB()
    data = db.read("SELECT * FROM nie.log;")
    db.close()
    return render_template('table.html', data=data)


if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0')
