from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL, ValidationError
from url_shortener.models import Link


class AddLinkForm(FlaskForm):
    full_link = StringField('Enter full URL', validators=[
                            DataRequired(), URL()])
    short_link = StringField('Short URL', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_short_link(self, short_link):
        link = Link.query.filter_by(short_link=short_link.data).first()
        if link:
            raise ValidationError('This URL is already taken')
