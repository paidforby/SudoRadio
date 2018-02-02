import os
from flask import Flask, request, render_template
import time
import datetime
import vlc
#import youtube_dl

app = Flask(__name__)

# Create a dictionary of scooters:

song = "/static/money.mp3"
art = "/static/incentivized_mesh_color_no_alpha.png"

@app.route('/')
def main():
	templateData = {
		'now_playing' : song,
		'now_playing_art' : art 
	}
	return render_template('main.html', **templateData)

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/", methods=['POST'])
def song_request():
        song = request.form['text']
        process = song.upper()
	return process 


if __name__ == '__main__':
	app.run(debug=True, use_reloader=False, host='0.0.0.0')

