import ast
import os
from flask import render_template, url_for
from money import Money
from app import app
from app.models import MovieCast, Crew, Talent
from app.service import movie as movie_service


@app.route('/movies/<m_id>')
def movies(m_id=1893):
    movie = movie_service.get_movie_detail(m_id)
    if movie:
        return render_template('movies.html', title='Movies', page_name='Movies', movie=movie,
                               dated_url_for=dated_url_for)
    else:
        message = 'Movie with id={} not found'.format(m_id)
        return render_template('index.html', title='Filmography', page_name='Movies', message=message,
                               dated_url_for=dated_url_for)


@app.route('/talent/<talent_id>')
def talent(talent_id=23659):
    talent_id = int(talent_id)

    talent_info = Talent.query.filter_by(id=talent_id).first()
    Talent.close_session()
    crew_member_info = Crew.query.filter_by(id=talent_id).all()
    Crew.close_session()
    cast_member_info = MovieCast.query.filter_by(id=talent_id).all()
    MovieCast.close_session()

    talent_data = dict()
    cast_data = dict()
    crew_data = dict()

    if talent_info:
        talent_data['name'] = talent_info.name
        talent_data['profile_path'] = talent_info.profile_path
        rev = Talent.cumulative_revenue(talent_id)
        rating = Talent.average_rating(talent_id)
        genres = Talent.genre_list(talent_id)
        Talent.close_session()
        talent_data['cumulative_revenue'] = Money(amount=rev, currency='USD') if rev else None
        talent_data['average_rating'] = round(rating, 2) if rating else None
        talent_data['genres'] = ", ".join([g[0] for g in genres]) if genres else None

        if cast_member_info:
            top_n_roles = Talent.top_ten_roles(talent_id)
            Talent.close_session()
            cast_data['primary_roles'] = top_n_roles if top_n_roles else None
        if crew_member_info:
            crew_roles = Talent.ten_crew_credits(talent_id)
            Talent.close_session()
            crew_data['crew_roles'] = crew_roles if crew_roles else None
        return render_template('talent.html', title='Talent', talent_data=talent_data, cast_data=cast_data,
                               crew_data=crew_data)
    else:
        message = 'Talent with id={} not found'.format(talent_id)
        return render_template('index.html', title='Filmography', page_name='Talent', message=message,
                               dated_url_for=dated_url_for)


@app.route('/')
@app.route('/graph/<n>')
@app.route('/graph')
def graph(n=20):
    # temporarily limit number of nodes in view
    # n = 30 if int(n) > 30 else int(n)
    # links_data, nodes_data = Nodes.get_links_and_nodes(n)
    # links_data = GraphData.links_data
    # nodes_data = GraphData.nodes_data
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
