#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states():
    """Display a HTML page with a list of all states"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>')
def states_id(id):
    """Display a HTML page with information about a state and its cities"""
    state = storage.get(State, id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
