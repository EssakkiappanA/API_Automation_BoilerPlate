import sys
from os import environ
import os
import pytest
from pytest_bdd import given, when
sys.path.append("tests-api")
from test_data import ReadData
from common.page_objects import APIGenerics

# from common.utils.property_parser import PropertyParser
# from common.utils.env_variables import EnvVariables
# from common.page_objects.api_generics import APIGenerics

import requests as requests
import logging
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
config_path = os.path.join(os.getcwd(), ".local.env")

load_dotenv(dotenv_path=config_path, verbose=True)


@given('I am using <auth_type>')
def using_auth_type(auth_type):
    pytest.globalDict['auth_type'] = auth_type
    print(f"Auth type:{os.getenv(auth_type)}")


@when('I call for <verb> <endpoint> <queryparam> <body>')
def call_api(base_url, verb, endpoint, queryparam, body):
    if verb == 'GET':
        APIGenerics.get_api(base_url, endpoint, queryparam, body)

    if verb == 'POST':
        APIGenerics.post_api(base_url, endpoint, queryparam, body)
        # body_data = ReadData.read_json(body)
        # print("*******Body Data********")
        # print(body_data)

    # if queryparam == '':
    #     response = requests.get(f'{base_url}{endpoint}', verify=False) #headers={"Authorization": "token %s" % token}, verify=False)
    # else:
    #     response = requests.get(f'{base_url}{endpoint}?{queryparam}', verify=False) #headers={"Authorization": "token %s" % token}, verify=False)

    # pytest.globalDict['response'] = response
