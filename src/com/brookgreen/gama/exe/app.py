import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

load_dotenv(find_dotenv())

app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_pre_ping": True}
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config["SQLALCHEMY_POOL_SIZE"] = 10
app.config["SQLALCHEMY_MAX_OVERFLOW"] = 20
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

db = SQLAlchemy(app)
