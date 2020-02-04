from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/quote')
def hello_world():
    artist = {'artist_name': 'Derp State Derptones'}
    if 'artist_name' in request.args:
        artist['artist_name'] = request.args.get('artist_name')
    return render_template('quote.html', artist=artist)


if __name__ == '__main__':
    app.run()
