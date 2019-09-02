import ast
import os
from flask import render_template, url_for
from money import Money
from app import app
from app.models import MoviesMetadata, MovieCollection, Ratings


@app.route('/')
def index():
    m_id = 862
    return render_template('index.html', title='Filmography', page_name='Movies', m_id=m_id,
                           dated_url_for=dated_url_for)


@app.route('/movies/<m_id>')
def movies(m_id=862):
    # Movies.query.filter(Movies.id == '862').all()
    movie_id = int(m_id)
    movies = MoviesMetadata.query.get(movie_id)

    if movies:
        movies_dir = dir(movies)
        movie_collection = MovieCollection.query.filter_by(film_id=movie_id).first()

        # related films
        related_films = MoviesMetadata.query.filter_by(collection_id=movies.collection_id).all()
        related_films = [rf for rf in related_films if rf.id != movie_id]
        avg_rating = Ratings.average(movie_id)

        if movies.revenue:
            formatted_revenue = Money(amount=movies.revenue, currency='USD')
        else:
            formatted_revenue = Money(amount=0, currency='USD')

        if movies.spoken_languages:
            spoken_languages = ast.literal_eval(movies.spoken_languages)
        else:
            spoken_languages = None

        if movies.budget:
            # TODO: location aware and correct currency
            formatted_budget = Money(amount=movies.budget, currency='USD')
        else:
            formatted_budget = Money(amount=0, currency='USD')

        movies_meta = dict()
        movies_meta['spoken_languages'] = spoken_languages
        movies_meta['formatted_budget'] = formatted_budget
        movies_meta['formatted_revenue'] = formatted_revenue
        movies_meta['related_films'] = related_films
        movies_meta['avg_rating'] = avg_rating

        return render_template('movies.html', title='Movies', page_name='Movies', movies=movies, movies_dir=movies_dir,
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
