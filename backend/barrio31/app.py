import logging
from logging.config import dictConfig

from flask import Flask, jsonify, request
from backend.barrio31.database.data_base import Database


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
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


if __name__ == '__main__':
    app.run()
