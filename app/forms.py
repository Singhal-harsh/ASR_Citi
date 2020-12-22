from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired


class RecordSampleForm(FlaskForm):
    soeid = StringField('Username', validators=[DataRequired()])
    query = SelectField("Query")
    submit = SubmitField('Submit')


class AddQueryForm(FlaskForm):
    soeid = StringField('Username', validators=[DataRequired()])
    query = StringField("Query", validators=[DataRequired()])
    submit = SubmitField('Submit')
