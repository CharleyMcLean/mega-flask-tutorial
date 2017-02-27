# ~/src/flask-tutorial/microblog/app/__init__.py
from flask import Flask

# Create the application object of class Flask
# This is the app variable which gets assigned to the Flask instance
app = Flask(__name__)
# Tell Flask to read and use the config file
app.config.from_object('config')


# Import views module.
# This is the app package which we import from the views module
# import is at the end to avoid circular references
from app import views
