# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv

import requests
import shutil
import tarfile
import os

output_filepath = '../../data/raw/'

def main():
    """ 
        Get data from:
            http://codeandbeer.org/virtual/BigData/Datasets/cryptocurrencypricehistory.tgz   
        into (../data/raw)
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    base_url = "http://codeandbeer.org/virtual/BigData/Datasets/"
    filename = "cryptocurrencypricehistory.tgz"

    response = requests.get(base_url+filename, stream=True)
    if response.status_code == 200:
        tarfile.open(fileobj=response.raw, mode="r|gz").extractall(output_filepath)
        #with open(output_filepath+"/"+filename, 'wb') as f:
            #f.write(response.raw.read())

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
