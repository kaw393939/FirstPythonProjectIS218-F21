"""A simple flask web app"""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    """Index Route Response"""
    return "<p>Hello, World!sdfdfdafs</p>"
