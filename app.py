from flask import Flask, Response
import requests

app = Flask(__name__)

# WSCR / The Score stream (AAC source)
STREAM_URL = "https://live.amperwave.net/direct/audacy-wscramaac-imc"

@app.route("/")
def home():
    return "WSCR Yoto relay is running"

@app.route("/wscr.mp3")
def stream():
    r = requests.get(STREAM_URL, stream=True)

    def generate():
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                yield chunk

    return Response(generate(), content_type="audio/mpeg")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
