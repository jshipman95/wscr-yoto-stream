from flask import Flask, Response
import subprocess

app = Flask(__name__)

# WSCR / 670 The Score AAC stream
STREAM_URL = "https://live.amperwave.net/direct/audacy-wscramaac-imc"

@app.route("/")
def home():
    return "WSCR MP3 relay running"

@app.route("/wscr.mp3")
def stream():
    process = subprocess.Popen(
        [
            "ffmpeg",
            "-i", STREAM_URL,      # input AAC stream
            "-f", "mp3",           # output format
            "-ab", "128k",         # bitrate
            "-acodec", "libmp3lame",
            "-content_type", "audio/mpeg",
            "-"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        bufsize=10**8
    )

    return Response(
        process.stdout,
        content_type="audio/mpeg",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive"
        }
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
