import ast
import os
from flask import render_template, url_for
from money import Money
from app import app
from app.models import MoviesMetadata, MovieCollection, Ratings, Genres, MovieCast, Crew, Talent
import numpy as np
import json


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
        movies_meta = dict()
        movie_collection = MovieCollection.query.filter_by(film_id=movie_id).first()

        # related films
        related_films = MoviesMetadata.query.filter_by(collection_id=movie.collection_id).all()
        related_films = [rf for rf in related_films if rf.id != movie_id]
        avg_rating = Ratings.average(movie_id)

        # genres
        genres = Genres.query.filter_by(film_id=movie_id).all()
        genre_list = ", ".join([g.name for g in genres]) if genres else None

        # directors
        directors = MoviesMetadata.directors(movie_id)
        movies_meta['directors'] = directors if directors else None

        # cast
        top_10_cast = MoviesMetadata.cast(movie_id)
        movies_meta['cast'] = top_10_cast if top_10_cast else None

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


@app.route('/talent/<talent_id>')
def talent(talent_id=524):
    talent_id = int(talent_id)

    talent_info = Talent.query.filter_by(id=talent_id).first()
    crew_member_info = Crew.query.filter_by(id=talent_id).all()
    cast_member_info = MovieCast.query.filter_by(id=talent_id).all()

    talent_data = dict()
    cast_data = dict()
    crew_data = dict()

    if talent_info:
        talent_data['name'] = talent_info.name
        talent_data['profile_path'] = talent_info.profile_path
        rev = Talent.cumulative_revenue(talent_id)
        rating = Talent.average_rating(talent_id)
        genres = Talent.genre_list(talent_id)
        talent_data['cumulative_revenue'] = Money(amount=rev, currency='USD') if rev else None
        talent_data['average_rating'] = round(rating, 2) if rating else None
        talent_data['genres'] = ", ".join([g[0] for g in genres]) if genres else None

        if cast_member_info:
            top_n_roles = Talent.top_ten_roles(talent_id)
            cast_data['primary_roles'] = top_n_roles if top_n_roles else None
        # if crew_member_info:
        # display additional info for crew
        return render_template('talent.html', title='Talent', talent_data=talent_data, cast_data=cast_data)
    else:
        message = 'Talent with id={} not found'.format(talent_id)
        return render_template('index.html', title='Filmography', page_name='Talent', message=message,
                               dated_url_for=dated_url_for)


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
