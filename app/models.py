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

    @staticmethod
    def genre_list(talent_id):
        query_string = """select distinct name
                            from genres where film_id in (
                                select distinct film_id
                                from movie_cast
                                where movie_cast.id = {}
                                union
                                distinct
                                select distinct film_id
                                from crew
                                where crew.id = {})
                                order by name""".format(talent_id, talent_id)
        sql = text(query_string)
        result = engine.execute(sql).fetchall()
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


class MovieCollection(Base):
    __table__ = Base.metadata.tables['movie_collection']
    __table_args__ = {'extend_existing': True}
    db_session = scoped_session(sessionmaker(bind=engine))
    query = db_session.query_property()

    def __repr__(self):
        return '<MovieCollection {}>'.format(self.name)
