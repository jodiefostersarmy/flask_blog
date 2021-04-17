import os
import tempfile

import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    db_fd, db_path = tempfile.mkstemp()         # opens a temp file, returns file object and path to it.

    app = create_app({
        'TESTING': True,                        # tells Flask that app is in TEST mode.
        'DATABASE': db_path,                    # DATABASE path overridden to point to the temp path instead of instance folder
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)

    yield app

    os.close(db_fd)                             # once done, the temp database is closed
    os.unlink(db_path)


@pytest.fixture
def client(app):                                # tells flask to use the client and not run the server
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client
    
    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login', 
            data={'username': username, 'password': password}
        )
    def logout(self):
        return self._client.get('/auth/logout')

@pytest.fixture
def auth(client):
    return AuthActions(client)