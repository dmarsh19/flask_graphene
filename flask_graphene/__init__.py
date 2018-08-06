"""
"""
import os
import logging

from flask import Flask
from flask.logging import default_handler
from flask_sqlalchemy import SQLAlchemy


root = logging.getLogger()
# create the application object
app = Flask(__name__)
# pulls in app configuration from settings.py
app.config.from_object("settings")

try:
    handler = logging.FileHandler(app.config["LOGFILE"], mode="a+", delay=True)
    handler.setFormatter(logging.Formatter("%(asctime)s|%(name)s|%(levelname)s|%(message)s"))
    try:
        if app.config["DEBUG"]:
            level = logging.DEBUG
        else:
            level = logging.INFO
    except KeyError:
        level = logging.DEBUG
    handler.setLevel(level)
except KeyError:
    handler = default_handler
root.addHandler(handler)

db = SQLAlchemy(app)

# import modules (have to import at the end after all app configurations are instantiated)
from .base import blueprint_base
from .api import blueprint_api

# register the individual blueprints (modules) to the app
app.register_blueprint(blueprint_base)
app.register_blueprint(blueprint_api, url_prefix="/api")

