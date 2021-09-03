from tools.credentials import get_credentials


def test_get_credentials_default():
    credentials = get_credentials(filename='tests/credentials.ini')
    assert credentials == {'username': 'user', 'password': 'pass'}


def test_get_credentials_profile():
    credentials = get_credentials(profile='dev', filename='tests/credentials.ini')
    assert credentials == {'username': 'devuser', 'password': 'devpass'}
