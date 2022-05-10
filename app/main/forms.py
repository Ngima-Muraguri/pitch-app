from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField
from wtforms.validators import DataRequired, Length

class Pitches(FlaskForm):
    title =StringField('Title',validators=[DataRequired(),Length(min=2, max=20)],render_kw={"placeholder": "Title"})
    description = TextAreaField('Description', validators=[DataRequired(),Length(min=2, max=200)],render_kw={"placeholder": "What's the pitch about"})
    submit = SubmitField('Publish')