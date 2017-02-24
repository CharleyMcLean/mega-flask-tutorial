# ~/src/flask-tutorial/microblog/app/views.py

# render_template function takes a template filename and a variable
# list of template arguments and returns the rendered template,
# with args replaed. Invokes the Jinja2 templating engine as part
# of the Flask framework.
from flask import render_template
from app import app

# Views are the handlers that respond to requests from web browsers or
# other clients.  In Flask, handlers are written as Python functions.
# Each view function is mapped to one or more request URLs

# These two route decorators above the function create the mappings from
# URLs '/' and '/index' to this function.
@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Alex'}
    posts = [
        {
            'author': {'nickname': 'Heidi'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Becca'},
            'body': 'Schnerdy rocks!'
        }
    ]
    return render_template('index.html',
                           title='Home',
                           user=user,
                           posts=posts)
