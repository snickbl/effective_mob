
from flask import Flask, Response   
import os

app = Flask(__name__)

@app.route("/")
def home():
    return Response("Hello from Effective Mobile!", mimetype="text/plain")

@app.route("/health")
def health():
    return Response("OK", status=200)

if __name__ == "__main__":
    debug = os.getenv("DEBUG", "false").lower() == "true"
    app.run(host="0.0.0.0", port=8080, debug=debug)
