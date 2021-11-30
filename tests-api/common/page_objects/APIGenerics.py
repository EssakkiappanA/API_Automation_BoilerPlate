import logging
from os import environ
import sys

import pytest
import re

import requests
from hamcrest import *

sys.path.append("tests-api")
from test_data import ReadData

logger = logging.getLogger(__name__)


def get_api(base_url, endpoint, queryParam, bodyData):
    # print("**********************GET METHOD*****************")
    auth_type = pytest.globalDict['auth_type']
    if auth_type == '':
        token = ''
    elif auth_type == 'basic':
        username = environ.get("BASIC_AUTH_USERNAME")
        password = environ.get("BASIC_AUTH_PASSWORD")
    elif auth_type == 'OAUTH1':
        token = environ.get("OAUTH1_TOKEN")
    elif auth_type == 'OAUTH2':
        token = environ.get("TERLLO_TOKEN")
        key = environ.get("TERLLO_KEY")
    else:
        token = environ.get("GITHUB_TOKEN")

    if queryParam == '':
        response_data = requests.get(f'{base_url}{endpoint}', verify=False) #headers={"Authorization": "token %s" % token}, verify=False)
    else:
        response_data = requests.get(f'{base_url}{endpoint}?{queryParam}', verify=False) #headers={"Authorization": "token %s" % token}, verify=False)

    pytest.globalDict['response'] = response_data
    logger.info("response details")
    logger.info(response_data.text)

def post_api(base_url, endpoint, queryParam, bodyData):
    # print("**********************POST METHOD*****************")
    auth_type = pytest.globalDict['auth_type']
    if auth_type == '':
        token = ''
    elif auth_type == 'basic':
        username = environ.get("BASIC_AUTH_USERNAME")
        password = environ.get("BASIC_AUTH_PASSWORD")
    elif auth_type == 'OAUTH1':
        token = environ.get("OAUTH1_TOKEN")
    elif auth_type == 'OAUTH2':
        token = environ.get("TERLLO_TOKEN")
        key = environ.get("TERLLO_KEY")
    else:
        token = environ.get("GITHUB_TOKEN")

    body_data = ReadData.read_json(bodyData)

    if queryParam == '':
        response_data = requests.post(f'{base_url}{endpoint}', json=body_data, verify=False) #headers={"Authorization": "token %s" % token}, verify=False)
    else:
        response_data = requests.get(f'{base_url}{endpoint}?{queryParam}', verify=False) #headers={"Authorization": "token %s" % token}, verify=False)

    pytest.globalDict['response'] = response_data
    logger.info("response details")
    logger.info(response_data.text)
