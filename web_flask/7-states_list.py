#!/usr/bin/python3
"""Module for script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Function that displays an HTML"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown_database():
    """Function that closes storage"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
