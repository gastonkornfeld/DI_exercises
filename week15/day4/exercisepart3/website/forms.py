  
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class SignUpForm(FlaskForm):
    username = StringField('Username',
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password1 = PasswordField('Password',
                        validators=[DataRequired()])
    password2 = PasswordField('Repeat password',
                        validators=[DataRequired(), EqualTo(password1)])
    name = StringField('Complete Name',
                        validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=2, max=20)])
    password = PasswordField('Password',
                        validators=[DataRequired()])
    submit = SubmitField('Login')

class AddFilmForm(FlaskForm):

    name = StringField('Film Title', validators=[DataRequired()])
    
    year = StringField('Date of release', validators=[DataRequired()])
    created_in = StringField('Country of creation', validators=[DataRequired()])
    categories = StringField('ADD categories separated by ","', validators=[DataRequired()])
    director = StringField('Imput Director Name, Last name ', validators=[DataRequired()])
    submit = SubmitField('Submit')



class AddDirectorForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Submit')



class SearchCategoryForm(FlaskForm):
    name = StringField('Category', validators=[DataRequired()])
    
    submit = SubmitField('Search')

