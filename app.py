from flask import Flask, Response
import requests

app = Flask(__name__)

# WSCR / 670 The Score AAC stream
STREAM_URL = "https://live.amperwave.net/direct/audacy-wscramaac-imc"

@app.route("/")
def home():
    return "WSCR relay running"

@app.route("/wscr.aac")
def stream():
    r = requests.get(STREAM_URL, stream=True)

    def generate():
        for chunk in r.iter_content(chunk_size=4096):
            if chunk:
                yield chunk

    return Response(
        generate(),
        content_type="audio/aac",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
