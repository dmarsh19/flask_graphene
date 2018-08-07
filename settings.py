import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

LOGFILE = '/var/log/flask_graphene/flask_graphene.log'

SQLALCHEMY_DATABASE_URI = "sqlite:///{}/atmo.sqlite".format(basedir)
SQLALCHEMY_TRACK_MODIFICATIONS = False
