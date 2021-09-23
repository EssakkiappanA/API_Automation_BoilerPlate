from os import environ
import pytest
from pytest_bdd import given, when
# from common.page_objects.api_generics import APIGenerics

import requests as requests
import logging

logger = logging.getLogger(__name__)


@given('I am using <auth_type>')
def using_auth_type(auth_type):
    pytest.globalDict['auth_type'] = auth_type


@when('I call for <verb> <endpoint>')
def call_api(base_url, verb, endpoint):
    auth_type = pytest.globalDict['auth_type']
    if auth_type == '':
        token = ''
    else:
        token = environ.get("GITHUB_TOKEN")

    # if verb == 'GET':
    print("inside the GET method")
    response = requests.get(f'{base_url}{endpoint}', verify=False) #headers={"Authorization": "token %s" % token}, verify=False)
    # logger.info("response---")
    # logger.debug("response---")
    print(response.text)
    # elif verb == 'POST':
    #     response = 'null'
    # elif verb == 'PUT':
    #     response = 'null'

    pytest.globalDict['response'] = response
