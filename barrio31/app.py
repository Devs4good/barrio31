import logging
from logging.config import dictConfig

from flask import Flask, jsonify, request
from barrio31.database.data_base import Database
from barrio31.services.places_service import PlacesService

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


@app.route('/places/<place_id>', methods=['GET', 'DELETE'])
def map_places(place_id):
    if request.method == 'GET':
        place = PlacesService.get_place(place_id)
        return jsonify(place.to_json()), 200
    elif request.method == 'DELETE':
        pass

    else:
        pass


@app.route('/places', methods=['GET', 'POST', 'DELETE'])
def map_places_all():
    if request.method == 'GET':
        entries = request.args.get('entries', None)
        place = PlacesService.get_all(entries)
        return jsonify(place), 200

    elif request.method == 'POST':
        place_attributes = request.get_json()
        logging.info(place_attributes)
        place = PlacesService.create_place(place_attributes)
        return jsonify(place.to_json()), 201

    elif request.method == 'DELETE':
        pass

    else:
        pass

if __name__ == '__main__':
    app.run()
