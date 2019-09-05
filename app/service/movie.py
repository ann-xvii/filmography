import ast

from money import Money

from app.errors import QueryException
from app.models import MovieCollection, MoviesMetadata, Ratings, Genres


class MovieDetail(object):
    def __init__(self, movie_id):
        self.movie_id = int(movie_id)
        self.movie_obj = None
        self.movie_collection = None
        self.related_films = None
        self.avg_rating = None
        self.genre_list = None
        self.directors = None
        self.cast = None
        self.formatted_revenue = None
        self.formatted_budget = None
        self.spoken_languages = None

        self.get_movie_object()
        self.get_collection()
        self.get_related_films()
        self.get_avg_rating()
        self.get_genre_list()
        self.get_directors()
        self.get_cast()
        self.get_revenue()
        self.get_spoken_languages()
        self.get_budget()

    def get_movie_object(self):
        try:
            self.movie_obj = MoviesMetadata.query.get(self.movie_id)
        except QueryException as e:
            self.movie_obj = None

    def get_collection(self):
        try:
            self.movie_collection = MovieCollection.query.filter_by(film_id=self.movie_id).first()
            MovieCollection.close_session()
        except QueryException as e:
            self.movie_collection = None

    def get_related_films(self):
        try:
            related_films = MoviesMetadata.query.filter_by(collection_id=self.movie_obj.collection_id).all()
            MoviesMetadata.close_session()
            self.related_films = [rf for rf in related_films if rf.id != self.movie_id]
        except QueryException as e:
            self.related_films = None

    def get_avg_rating(self):
        try:
            self.avg_rating = Ratings.average(self.movie_id)
            Ratings.close_session()
        except QueryException as e:
            self.avg_rating = None

    def get_genre_list(self):
        try:
            genres = Genres.query.filter_by(film_id=self.movie_id).all()
            Genres.close_session()
            self.genre_list = ", ".join([g.name for g in genres]) if genres else None
        except QueryException as e:
            self.genre_list = None

    def get_directors(self):
        try:
            directors = MoviesMetadata.directors(self.movie_id)
            MoviesMetadata.close_session()
            self.directors = directors if directors else None
        except QueryException as e:
            self.directors = None

    def get_cast(self):
        try:
            top_10_cast = MoviesMetadata.cast(self.movie_id)
            MoviesMetadata.close_session()
            self.cast = top_10_cast if top_10_cast else None
        except QueryException as e:
            self.cast = None

    def get_revenue(self):
        self.formatted_revenue = Money(amount=self.movie_obj.revenue,
                                       currency='USD') if self.movie_obj.revenue else Money(
            amount=0,
            currency='USD')

    def get_spoken_languages(self):
        if self.movie_obj.spoken_languages:
            spoken_languages = ast.literal_eval(self.movie_obj.spoken_languages)
            lang_list = [g['name'] for g in spoken_languages]
            self.spoken_languages = ", ".join(lang_list)

    def get_budget(self):
        self.formatted_budget = Money(amount=self.movie_obj.budget, currency='USD') if self.movie_obj.budget else Money(
            amount=0,
            currency='USD')


def get_movie_detail(movie_id):
    movie = MovieDetail(movie_id)
    return movie if movie else None
