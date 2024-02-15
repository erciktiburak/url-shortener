from flask import Flask, redirect
from url_shortener import URLShortener

app = Flask(__name__)
url_shortener = URLShortener()

@app.route('/')
def index():
    return "Welcome to URL Shortener!"

@app.route('/favicon.ico')
def favicon():
    return "", 204

@app.route('/<short_url>')
def redirect_to_long_url(short_url):
    long_url = url_shortener.expand_url(short_url)
    if long_url:
        return redirect(long_url, code=301)
    else:
        return "URL not found", 404

if __name__ == "__main__":
    app.run()