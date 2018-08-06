"""
"""
from flask import Blueprint


blueprint_api = Blueprint("api", __name__)

from . import views

