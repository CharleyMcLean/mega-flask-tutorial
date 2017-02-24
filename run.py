# ~/src/flask-tutorial/microblog/run.py

#!flask/bin/python
# Imports app variable from our app package and invokes its run method
# to start the server
# The app variable holds the Flask instance we created in app/__init__.py
from app import app
app.run(debug=True)

#################################################
# to start the app, run the following:
# chmod a+x run.py
# ./run.py

# Open web browser to:
# http://localhost:5000
