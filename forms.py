from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectMultipleField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length

genres = [
    "Comedy", "Fantasy", "Crime", "Drama", "Music", "Adventure", "History",
    "Thriller", "Animation", "Family", "Mystery", "Biography", "Action",
    "Film-Noir", "Romance", "Sci-Fi", "War", "Western", "Horror", "Musical",
    "Sport"
]


class MovieForm(FlaskForm):

    title = StringField('Title',
                        validators=[DataRequired(),
                                    Length(min=1, max=50)])

    description = TextAreaField('Description', validators=[DataRequired()])

    genres = SelectMultipleField('Genres',
                                 validators=[DataRequired()],
                                 choices=[(genre, genre) for genre in genres])

    year = DateField('Year', validators=[DataRequired()])

    submit = SubmitField('Add')
