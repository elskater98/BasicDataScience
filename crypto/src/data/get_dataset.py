# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import requests
import shutil
import tarfile
import io

@click.command()
@click.argument('output_filepath', type=click.Path(exists=True))
def main(output_filepath):
    """ 
        Get data from:
            http://codeandbeer.org/virtual/BigData/Datasets/measures.tgz
        into (../data/raw)
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    base_url = "http://codeandbeer.org/virtual/BigData/Datasets/measures.tgz"
    r = requests.get(base_url, stream=True)
    if r.status_code == 200:
        opened_tar = tarfile.open(io.BytesIO(r.content))
        if tarfile.is_tarfile(opened_tar):
            opened_tar.extractall()

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
