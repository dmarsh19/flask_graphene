"""
"""
from flask import Blueprint


blueprint_base = Blueprint("base",
                           __name__,
                           template_folder='templates')

from . import views

