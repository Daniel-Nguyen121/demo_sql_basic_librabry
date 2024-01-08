## Imports ##
# Import framework Flask for creating web_based application
from flask import Flask
# Imports the Flask-CORS extension for handling Cross-Origin Resource Sharing (CORS).
# from flask_cors import CORS

# Import Flask-SQLAlchemy extension for working with SQL databases
from flask_sqlalchemy import SQLAlchemy
# Import configuration values from 'config' module
from config import SQLALCHEMY_DATABASE_URI
# from flask_migrate import Migrate
# from config import SECRET_KEY, DATA_PATH
# @-------------------------------------------@#

## Flask Application Creation ##
# Create a Flask application instance
app = Flask(__name__)
# @-------------------------------------------@#

## Configuration ##
# Set the database connection URI from the imported configuration
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# Enable tracking of model changes (may not be necessary in all cases).
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Set options for the SQLAlchemy engine, such as connection pool size.
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'max_overflow': 30,
    'pool_size': 100
}
# @-------------------------------------------@#

# Specifies the directory for uploaded files.
# app.config['UPLOAD_FOLDER'] = DATA_PATH
# Sets a secret key for securely signing cookies and other data
# app.secret_key = SECRET_KEY
## CORS Handling ##
# Configures CORS to allow requests from any origin.
# CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "False"}})
# @-------------------------------------------@#

## SQLAlchemy Integration ##
# Initialize SQLAlchemy for the application, disabling automatic commits and flushes.
db = SQLAlchemy(
    app=app,
    session_options={'autocommit': False, 'autoflush': False}
)
# @-------------------------------------------@#

## Migration Setup ##
# Initializes Flask-Migrate for managing database migrations.
# migrate = Migrate(app, db)
#  Ensures that the database connection is initialized within the application context.
# with app.app_context():
# Initializes the migration commands for the application.
#     migrate.init_app(app, db)
