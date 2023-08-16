#!/usr/bin/python3

"""A simple Flask application displaying 'states or cities' at the root."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return f'C {text.replace("_"," ")}'


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    return f'Python {text.replace("_"," ")}'


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f'{n} is number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    odd_or_even = "odd" if n % 2 != 0 else "even"
    return render_template('6-number_odd_or_even.html', number=n,
                           odd_even=odd_or_even)


@app.route("/states_list", strict_slashes=False)
def states_list():
    return render_template("7-states_list.html", states=storage.all(State))


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    return render_template("8-cities_by_states.html",
                           states=storage.all(State))


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_or_cities(id=None):
    states = storage.all(State).value()
    if id is not None:
        for state in states:
            if state.id == id:
                return render_template("9-states.html", states=state)
        return render_template("9-states.html")
    return render_template("9-states.html", states=states, full=True)


@app.teardown_appcontext
def teardown(e):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
