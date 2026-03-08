import os
import sys

# Add the application's directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask application object
from app import app as application

# Set the secret key if it's not already set
if not application.secret_key:
    application.secret_key = os.urandom(24)
