# ~/src/flask-tutorial/microblog/app/views.py

# render_template function takes a template filename and a variable
# list of template arguments and returns the rendered template,
# with args replaed. Invokes the Jinja2 templating engine as part
# of the Flask framework.
from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

# this view function accepts GET and POST requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    # We imported our LoginForm class, instantiated an object from it,
    # and sent it down to the template.
    form = LoginForm()

    # when validate_on_submit is called as part of a form submission request,
    # it will gather all data, run all validators attached to fields, and if
    # everything is ok it will return True, indicating data is valid
    # and can be processed - indicates data safe to incorporate into application
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              form.openid.data, str(form.remember_me.data))
        # Nav to diff page instead of the one requested
        return redirect('/index')

    # if at least one field fails validation function will return False
    # and cause form to be rendered back to user, giving the user a chance
    # to correct any mistakes
    # grab configuration by looking it up in app.config with its key
    return render_template('login.html',
                            title='Sign In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])


