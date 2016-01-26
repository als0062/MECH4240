import os
from flask import Flask, jsonify
from flask import url_for

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

from rh import views