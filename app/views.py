# ~/src/flask-tutorial/microblog/app/views.py
from app import app

# Views are the handlers that respond to requests from web browsers or
# other clients.  In Flask, handlers are written as Python functions.
# Each view function is mapped to one or more request URLs

# These two route decorators above the function create the mappings from
# URLs '/' and '/index' to this function.
@app.route('/')
@app.route('/index')
def index():
    return "Yo, what up world!"
