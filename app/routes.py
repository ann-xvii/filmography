import ast
import os
from flask import render_template, url_for
from money import Money
from app import app
from app.models import MoviesMetadata, MovieCollection, Ratings, Genres


@app.route('/')
def index():
    m_id = 862
    return render_template('index.html', title='Filmography', page_name='Movies', m_id=m_id,
                           dated_url_for=dated_url_for)


@app.route('/movies/<m_id>')
def movies(m_id=862):
    movie_id = int(m_id)
    movie = MoviesMetadata.query.get(movie_id)

    if movie:
        movies_dir = dir(movie)
        movie_collection = MovieCollection.query.filter_by(film_id=movie_id).first()

        # related films
        related_films = MoviesMetadata.query.filter_by(collection_id=movie.collection_id).all()
        related_films = [rf for rf in related_films if rf.id != movie_id]
        avg_rating = Ratings.average(movie_id)

        # genres

        genres = Genres.query.filter_by(film_id=movie_id).all()
        if genres:
            genre_list = [g.name for g in genres]
            genre_list = ", ".join(genre_list)
        else:
            genre_list = None

        if movie.revenue:
            formatted_revenue = Money(amount=movie.revenue, currency='USD')
        else:
            formatted_revenue = Money(amount=0, currency='USD')

        if movie.spoken_languages:
            spoken_languages = ast.literal_eval(movie.spoken_languages)
            lang_list = [g['name'] for g in spoken_languages]
            lang_list = ", ".join(lang_list)
        else:
            lang_list = None

        if movie.budget:
            # TODO: location aware and correct currency
            formatted_budget = Money(amount=movie.budget, currency='USD')
        else:
            formatted_budget = Money(amount=0, currency='USD')

        movies_meta = dict()
        movies_meta['spoken_languages'] = lang_list
        movies_meta['formatted_budget'] = formatted_budget
        movies_meta['formatted_revenue'] = formatted_revenue
        movies_meta['related_films'] = related_films
        movies_meta['avg_rating'] = avg_rating
        movies_meta['genre_list'] = genre_list

        return render_template('movies.html', title='Movies', page_name='Movies', movies=movie, movies_dir=movies_dir,
                               movie_collection=movie_collection, movies_meta=movies_meta,
                               dated_url_for=dated_url_for)
    else:
        message = 'Movie with id={} not found'.format(m_id)
        return render_template('index.html', title='Filmography', page_name='Movies', message=message,
                               dated_url_for=dated_url_for)


@app.route('/talent')
def talent():
    return render_template('talent.html', title='Talent', page_name='Talent')


@app.route('/graph')
def graph():
    return render_template('graph.html', title='Graph', page_name='Graph View')


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
