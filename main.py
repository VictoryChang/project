import logging

import click

from tools import get_credentials

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@click.command()
@click.option('--profile', default='default', show_default=True, help='Profile to use')
def main(profile):
    credentials = get_credentials(profile)
    logger.info(credentials)


if __name__ == '__main__':
    main()
