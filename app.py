from flask import Flask, request, render_template, redirect, url_for
from forms import MovieForm
from flask_sqlalchemy import SQLAlchemy
# from app import db

app = Flask(__name__)

db = SQLAlchemy(app)
# db = SQLAlchemy()
# db.init_app(app)


app.config["SECRET_KEY"] = '238be01f247e6114d1874911a63e6bfdb2db63ebc'
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///movies'

# CamelCase  ===> camel_case


movie_genre = db.Table(
    'movie_genre',
    db.Column('movie_id',
              db.Integer,
              db.ForeignKey('movie.id'),
              nullable=False,
              primary_key=True),
    db.Column('genre_id',
              db.Integer,
              db.ForeignKey('genre.id'),
              nullable=False,
              primary_key=True))


class Movie(db.Model):

    # __tablename__ = 'movies'

    id = db.Column(db.Integer, nullable=False, primary_key=True)

    title = db.Column(db.String(50), nullable=False, unique=True)

    description = db.Column(db.Text)

    year = db.Column(db.DateTime, nullable=False)

    genres = db.relationship('Genre',
                             backref='movie',
                             lazy=True,
                             secondary=movie_genre)

    def __str__(self):
        return 'Movie(id={}, title={})'.format(self.id, self.title)

    def __repr__(self):
        return 'Movie(id={}, title={})'.format(self.id, self.title)


class Genre(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)

    name = db.Column(db.String(50), nullable=False, unique=True)

    # movie_id = db.Column(db.Intger, db.ForeignKey('movie.id'), nullable=False)

    # movie = db.relationship('Movie', backref='genres', lazy=True)


genres = [
    "Comedy", "Fantasy", "Crime", "Drama", "Music", "Adventure", "History",
    "Thriller", "Animation", "Family", "Mystery", "Biography", "Action",
    "Film-Noir", "Romance", "Sci-Fi", "War", "Western", "Horror", "Musical",
    "Sport"
]


@app.route('/')
def index():
    return render_template('index.html', movies=Movie.query.all())


@app.route('/movie/<id>')
def show(id):
    movie = Movie.query.get(int(id))
    if not movie:
        return "not found"
    return render_template('show.html', movie=movie)


@app.route('/movie/add', methods=['GET', 'POST'])
def movie_form():
    form = MovieForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            m = Movie(title=form.title.data,
                      year=form.year.data,
                      description=form.description.data)

            db.session.add(m)
            db.session.commit()
            url_to_dedirect = url_for('index', id=m.id)
            return redirect(url_to_dedirect)
        else:
            return render_template('movie_form.html', form=form)
    else:
        return render_template('movie_form.html', form=form)


@app.route('/movie/delete/<id>')
def deleteMovie(id):
    # Movie.query.filter_by(Movie.id == int(id)).delete()
    # db.session.commit()
    mv = Movie.query.get(id)
    db.session.delete(mv)
    db.session.commit()
    url_to_dedirect = url_for('index')
    return redirect(url_to_dedirect)


# @app.route('/a')
# def a():
#     return redirect('/b')
# @app.route('/b')
# def b():
#     return redirect('/a')
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)
