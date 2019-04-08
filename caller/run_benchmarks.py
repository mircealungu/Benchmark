import configparser
import os

import perf
import requests

LOCATION = os.path.abspath(os.path.dirname(__file__)) + '/'
config = configparser.ConfigParser()
config.read(LOCATION + '../config.ini')

bm_info = configparser.ConfigParser()
bm_info.read(LOCATION + '../bm_info.ini')

APP_PATH = config['micro_app']['protocol'] + '://' +\
           config['micro_app']['url'] + ':' +\
           config['micro_app']['port'] + '/'


def call_endpoint(endpoint):
    r = requests.get(APP_PATH + endpoint)
    r.json()


if __name__ == "__main__":
    values = config['micro_run']['values']
    processes = config['micro_run']['processes']
    runner = perf.Runner(values=values, processes=processes)
    runner.metadata['description'] = bm_info['bench']['desc']
    runner.bench_func(bm_info['bench']['name'], call_endpoint, bm_info['bench']['name'])
