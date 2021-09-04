from pathlib import Path
import configparser
import os


def get_credentials(profile: str = 'default', filename: str ='~/.project/credentials'):
    config = configparser.ConfigParser()
    config.read(Path(filename).expanduser())
    return dict(config[profile])


def load_credentials(profile: str = 'default', filename: str ='~/.project/credentials'):
    credentials = get_credentials(profile, filename)
    os.environ.update(credentials)
