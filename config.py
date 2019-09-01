import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'filmography.db')
    DATABASE_URI = 'postgresql://{user}:{passwd}@{host}:{port}/filmography'.format(user=os.getenv('POSTGRES_USER'),
                                                                                   passwd=os.getenv('POSTGRES_PASS'),
                                                                                   host=os.getenv('POSTGRES_HOST'),
                                                                                   port=os.getenv('POSTGRES_PORT'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
