# -*- coding: utf-8 -*-
import logging
import shutil
from pathlib import Path

import click
import requests
from dotenv import find_dotenv, load_dotenv

output_filepath = '../../data/raw/'


@click.command()
def main():
    """ Gets data from:
        http://codeandbeer.org/virtual/BigData/Datasets/iris.data
        int (../data/raw).
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    baseurl = "http://codeandbeer.org/virtual/BigData/Datasets/"
    filename = "iris.data"
    r = requests.get(baseurl + "/" + filename, stream=True)
    if r.status_code == 200:
        with open(output_filepath + "/" + filename, "wb") as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
