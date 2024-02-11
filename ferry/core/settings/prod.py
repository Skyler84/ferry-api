# type: ignore
import os

from .base import *  # noqa: F403

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["SECRET_KEY"]

DATABASE = {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": os.environ.get("SQL_DATABASE"),
    "USER": os.environ.get("SQL_USER"),
    "PASSWORD": os.environ.get("SQL_PASSWORD"),
    "HOST": os.environ.get("SQL_HOST"),
    "PORT": os.environ.get("SQL_PORT"),
}

DISCORD_GUILD = os.environ["DISCORD_GUILD"]
DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
