# Web forms are rep'd in Flask-WTF as classes, subclasses from base class Form
# A form subclass simply defines the fields of the form as class variables
from flask_wtf import Form

# form field classes
from wtforms import StringField, BooleanField

# Function that can be attached to a field to perform validation on data
# submitted by the user.  DataRequired checks that field is not submitted empty
from wtforms.validators import DataRequired

# Create a login form that usrs will use to id with the system
# Login mechanism we'll support in our app is an OpenID
# OpenIDs have the benefit of having authentication done by the provider
# of the OpenID, so no validating passwords - more secure to users.
class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)