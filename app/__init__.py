import logging
import os

from flask import Flask
from dotenv import load_dotenv
from flask_bootstrap import Bootstrap

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
# database
db = SQLAlchemy(app)
# migration engine
migrate = Migrate(app, db)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
app.logger.addHandler(stream_handler)

from app import routes, models
