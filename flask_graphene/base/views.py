"""
"""
from flask import render_template

from . import blueprint_base


@blueprint_base.route("/")
def main():
    return render_template("base.html")

