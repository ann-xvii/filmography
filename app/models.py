from app import db
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.orm import relationship, backref, scoped_session, sessionmaker

# engine = create_engine('sqlite:///filmography.db', convert_unicode=True, echo=False)
engine = create_engine(
    'postgresql://{user}:{passwd}@{host}:{port}/filmography'.format(user=os.getenv('POSTGRES_USER'),
                                                                    passwd=os.getenv('POSTGRES_PASS'),
                                                                    host=os.getenv('POSTGRES_HOST'),
                                                                    port=os.getenv('POSTGRES_PORT')),
    convert_unicode=True, echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)


class MoviesMetadata(Base):
    __table__ = Base.metadata.tables['movies']

    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()


class Genres(Base):
    __table__ = Base.metadata.tables['genres']

    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()


class Crew(Base):
    __table__ = Base.metadata.tables['crew']

    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()


class MovieCast(Base):
    __table__ = Base.metadata.tables['movie_cast']

    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()


class Talent(Base):
    __table__ = Base.metadata.tables['talent']

    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()

    @staticmethod
    def cumulative_revenue(talent_id):
        query_string = """select sum(revenue)
                            from movies
                            where id in (
                                select distinct film_id
                                from movie_cast
                                where movie_cast.id = {}
                                union
                                distinct
                                select distinct film_id
                                from crew
                                where crew.id = {})""".format(talent_id, talent_id)
        sql = text(query_string)
        result = engine.execute(sql).first()
        if result:
            return result[0]
        return result

    @staticmethod
    def average_rating(talent_id):
        query_string = """select avg(rating)
                            from ratings
                            where movieId in (
                                select distinct film_id
                                from movie_cast
                                where movie_cast.id = {}
                                union
                                distinct
                                select distinct film_id
                                from crew
                                where crew.id = {}
)""".format(talent_id, talent_id)
        sql = text(query_string)
        result = engine.execute(sql).first()
        if result:
            return result[0]
        return result


class Ratings(Base):
    __table__ = Base.metadata.tables['ratings']

    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()

    @staticmethod
    def average(movie_id):
        query_string = """select avg(rating)
                            from ratings 
                            left join movies
                             on ratings.movieid = movies.id
                              where movieid={}""".format(
            movie_id)
        sql = text(query_string)
        result = engine.execute(sql).first()[0]
        if result:
            result = round(result, 1)
        return result


# class MoviesMetadata(db.Model):
#     __tablename__ = 'movies'
#     index = db.Column(db.BigInteger)
#     adult = db.Column(db.Text)
#     belongs_to_collection = db.Column(db.Text())
#     budget = db.Column(db.Text)
#     genres = db.Column(db.Text)
#     homepage = db.Column(db.Text)
#     id = db.Column(db.Integer, primary_key=True)
#     imdb_id = db.Column(db.String(50), index=True)
#     original_language = db.Column(db.String(100))
#     original_title = db.Column(db.Text, index=True)
#     overview = db.Column(db.Text)
#     popularity = db.Column(db.Float)
#     poster_path = db.Column(db.String(200))
#     production_companies = db.Column(db.Text)
#     production_countries = db.Column(db.Text)
#     release_date = db.Column(db.DateTime)
#     revenue = db.Column(db.Integer)
#     runtime = db.Column(db.Float)
#     spoken_languages = db.Column(db.Text)
#     status = db.Column(db.String(40))
#     tagline = db.Column(db.Text)
#     title = db.Column(db.Text, index=True)
#     video = db.Column(db.Boolean)
#     vote_average = db.Column(db.String)
#     vote_count = db.Column(db.Integer)
#     collection_id = db.Column(db.Integer, db.ForeignKey('movies.id'))  # collection has many movies
#
#     def __repr__(self):
#         return '<MovieMetadata {}>'.format(self.title)


# class Credit(db.Model):
#     __tablename__ = 'credits'
#     cast = db.Column(db.Text)
#     crew = db.Column(db.Text)
#     id = db.Column(db.Integer, db.ForeignKey('movies_metadata.id'), primary_key=True)
#
#     def __repr__(self):
#         return '<Credits {}>'.format(self.id)
#
#
# class Rating(db.Model):
#     __tablename__ = 'ratings'
#     user_id = db.Column(db.Integer, index=True)
#     movie_id = db.Column(db.Integer, db.ForeignKey('movies_metadata.id'), primary_key=True, index=True)
#     rating = db.Column(db.Float)
#     timestamp = db.Column(db.DateTime, index=True)
#
#     def __repr__(self):
#         return '<Ratings {}>'.format(self.movie_id)


class MovieCollection(Base):
    # __tablename__ = 'movie_collection'
    __table__ = Base.metadata.tables['movie_collection']
    __table_args__ = {'extend_existing': True}
    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()

    # index = db.Column(db.BigInteger)
    # backdrop_path = db.Column(db.Text)
    # film_id = db.Column(db.BigInteger, db.ForeignKey('movies.id'), primary_key=True)
    # id = db.Column(db.BigInteger, primary_key=True)
    # name = db.Column(db.Text)
    # poster_path = db.Column(db.Text)

    def __repr__(self):
        return '<MovieCollection {}>'.format(self.name)
