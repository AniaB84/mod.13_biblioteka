from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, IntegerField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    author = TextAreaField('author', validators=[DataRequired()])
    read = BooleanField('read', validators=[DataRequired()])
    id = IntegerField('id', validators=[DataRequired()])
   