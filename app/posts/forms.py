from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired, InputRequired


class PostForm(Form):
    title = StringField('Title', [InputRequired()])
    body = TextAreaField('Body', [InputRequired()])
