import datetime
import os

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
def home_page():
    now = datetime.datetime.now()
    return render_template('home.html', current_time=now.ctime())

@app.route('/login')
def login_page():
    return render_template('login.html')
@app.route('/team')
def team_page():
    return render_template('team.html')

@app.route('/player')
def player_page():
    return render_template('player.html')
@app.route('/statistics')
def statistics_page():
    return render_template('statistics.html')

    
if __name__ == '__main__':
     VCAP_APP_PORT = os.getenv('VCAP_APP_PORT')
     if VCAP_APP_PORT is None:
         port = int(VCAP_APP_PORT)
     else:
         port = 5000
         app.debug = True
     app.run(host='0.0.0.0', port=port)
