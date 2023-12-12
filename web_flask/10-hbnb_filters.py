#!/usr/bin/python3
"""Web App with Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display HBNB filters"""
    states = storage.all(State)
    amenity = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenity)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
