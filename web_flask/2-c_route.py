#!/usr/bin/python3
"""Module for script that starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function that displays Hello HBNB!"""

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that displays HBNB"""

    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text=None):
    """Function that displays C followed by the value of the text variable"""

    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")