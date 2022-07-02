import os

basedir = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
                           basedir, '..', 'allabouttravel.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = 'fsdfdvcxvdgfdfbvcbnnfgnffngnfgnfbv'