from flask import Flask, request, render_template
import youtube_dl

app = Flask(__name__)
ytdl_opts = {
        'outtmpl': 'static/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
        }],
        'writethumbnail' : "art"
}

ytdl = youtube_dl.YoutubeDL(ytdl_opts)

song = "bonobo-kerala"

@app.route('/')
def main():
	templateData = {
		'now_playing' : song
	}
	return render_template('main.html', **templateData)

@app.route("/", methods=['POST'])
def song_request():
        song = request.form['song']
        info = ytdl.extract_info(song) # this also downloads the video
        print info['webpage_url']
        templateData = {
                'now_playing' : info['title']
        }
        return render_template('main.html', **templateData)
        
if __name__ == '__main__':
	app.run(debug=True, use_reloader=False, host='0.0.0.0')

