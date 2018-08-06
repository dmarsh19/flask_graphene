import os

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

LOGFILE = '/var/log/flask_graphene/flask_graphene.log'

SQLALCHEMY_DATABASE_URI = "sqlite:///{}/atmo.sqlite".format(basedir)
