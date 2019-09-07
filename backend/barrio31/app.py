import logging
from logging.config import dictConfig

from flask import Flask, jsonify, request
from database.data_base import Database
from services.places_service import PlacesService

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'local': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['local']
    }
})


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_pyfile("config.py")
    return flask_app

app = create_app()
Database(app.config)


@app.route('/ping')
def hello_world():
    return jsonify(dict(pong="Pong")), 200


@app.route('/places', methods=['GET', 'POST', 'DELETE'])
def map_places(place_id):
    if request.method == 'GET':
        place = PlacesService.get_place(place_id)
        return jsonify(place), 200

    elif request.method == 'POST':
        place_attributes = request.get_json()
        place = PlacesService.create_place(place_attributes)
        return jsonify(place), 201

    elif request.method == 'DELETE':
        pass

    else:
        pass


if __name__ == '__main__':
    app.run()
