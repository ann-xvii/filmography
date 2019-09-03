import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'filmography.db')
    # DATABASE_URL = 'postgresql://{user}:{passwd}@{host}:{port}/filmography'.format(user=os.environ.get('POSTGRES_USER'),
    #                                                                                passwd=os.environ.get('POSTGRES_PASS'),
    #                                                                                host=os.environ.get('POSTGRES_HOST'),
    #                                                                                port=os.environ.get('POSTGRES_PORT'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')


