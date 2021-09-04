import logging
import os

import click

from tools.credentials import load_credentials

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@click.command()
@click.option('--profile', default='default', show_default=True, help='Profile to use')
def main(profile):
    load_credentials(profile)
    logger.info(os.environ['username'])


if __name__ == '__main__':
    main()
