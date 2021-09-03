from pathlib import Path
import configparser


def get_credentials(profile: str = 'default', filename: str ='~/.project/credentials'):
    config = configparser.ConfigParser()
    config.read(Path(filename).expanduser())
    return dict(config[profile])
