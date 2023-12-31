import os
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# Create the SQLAlchemy instance at the top level, not bound to any specific app yet


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Environment variables for database configuration, not best practice , to move to .env file later on
    db_user = os.environ.get('DB_USER')
    db_password = os.environ.get('DB_PASSWORD')
    db_host = os.environ.get('DB_HOST')
    db_name = os.environ.get('DB_NAME')
    db_port = os.environ.get('DB_PORT')

    # db_user = os.environ.get('DB_USER', 'postgres')

    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        SQLALCHEMY_DATABASE_URI=f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}',
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

    # Initialize the SQLAlchemy instance with the app
    from .models import db
    db.init_app(app)
    migrate = Migrate(app, db)

    from .api import stocks, prices
    app.register_blueprint(prices.bp)
    app.register_blueprint(stocks.bp)

    return app
