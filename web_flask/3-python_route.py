#!/usr/bin/python3

"""A simple Flask application displaying 'python_route' at the root."""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "<p>Hello HBNB!</p>"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "<p>HBNB</p>"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return f'C {text.replace("_"," ")}'


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    return f'Python {text.replace("_"," ")}'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
