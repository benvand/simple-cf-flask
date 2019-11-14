import os

from flask import Flask
from flask.json import jsonify
from flask_basicauth import BasicAuth


class Config(object):
    DEBUG = False
    TESTING = False
    BASIC_AUTH_USERNAME = os.getenv('BASIC_AUTH_USERNAME')
    BASIC_AUTH_PASSWORD = os.getenv('BASIC_AUTH_PASSWORD')


app = Flask(__name__)
app.config.from_object(Config)

basic_auth = BasicAuth(app)


@app.route('/')
@basic_auth.required
def index():
    return 'Hello, World!', 200


@app.route('/_status')
def status():
    return jsonify({'status': 'OK'}), 200