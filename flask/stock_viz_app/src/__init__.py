import os
import io
from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import google.auth
from google.cloud import secretmanager as sm
import environ
from flask_cloudy import Storage

# Load environment variables from .env file
load_dotenv()

# Google Cloud Secret Manager integration
SETTINGS_NAME = "application_settings"

_, project = google.auth.default()
client = sm.SecretManagerServiceClient()
name = f"projects/{project}/secrets/{SETTINGS_NAME}/versions/latest"
payload = client.access_secret_version(name=name).payload.data.decode("UTF-8")

env = environ.Env()
env.read_env(io.StringIO(payload))

# Flask application factory


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Set Flask configuration from environment variables
    app.config.from_mapping(
        SECRET_KEY=env("SECRET_KEY", default='dev'),
        SQLALCHEMY_DATABASE_URI=env("DATABASE_URL"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SQLALCHEMY_ECHO=True
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Cloud Run Service URL check (similar to Django's ALLOWED_HOSTS)
    CLOUDRUN_SERVICE_URL = env("CLOUDRUN_SERVICE_URL", default=None)
    if CLOUDRUN_SERVICE_URL:
        @app.before_request
        def limit_remote_addr():
            if request.host != CLOUDRUN_SERVICE_URL:
                abort(403)  # Forbidden

    # Configure Google Cloud Storage for static files
    GS_BUCKET_NAME = env("GS_BUCKET_NAME")
    # Conditionally configure Google Cloud Storage
    google_cloud_storage_secret = env(
        "GOOGLE_CLOUD_STORAGE_SECRET", default=None)
    if google_cloud_storage_secret:
        app.config['STORAGE_PROVIDER'] = 'GOOGLE_STORAGE'
        app.config['STORAGE_KEY'] = env("GOOGLE_CLOUD_STORAGE_KEY")
        app.config['STORAGE_SECRET'] = google_cloud_storage_secret
        app.config['STORAGE_CONTAINER'] = env("GS_BUCKET_NAME")
        app.config['STORAGE_SERVER'] = True  # Serve files directly

    storage = Storage()
    storage.init_app(app)

    # Initialize the SQLAlchemy instance with the app
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    # Define your blueprints and routes here
    # Example:
    from .api import stocks, prices
    app.register_blueprint(prices.bp)
    app.register_blueprint(stocks.bp)

    return app
