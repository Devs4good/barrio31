
import logging

from flask import Flask, jsonify, request


def create_app():
    flask_app = Flask(__name__)
    return flask_app


app = create_app()


@app.route('/ping')
def hello_world():
    return jsonify(dict(pong="Pong")), 200


if __name__ == '__main__':
    app.run()
