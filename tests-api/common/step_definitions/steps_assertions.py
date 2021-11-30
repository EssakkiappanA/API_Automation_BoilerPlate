import logging

import pytest
import json
from jsonpath_ng import jsonpath, parse
# from assertpy import assert_that
from pytest_bdd import then
from hamcrest import *


@then('I get <response_code> and <response_message>')
def validate_response(base_url, response_code, response_message):
    response = pytest.globalDict['response']

    assert_that(response.status_code).is_equal_to(int(response_code))
    assert_that(response.text).is_equal_to_ignoring_case(response_message)


@then('I get <response_code>')
def validate_response_code(base_url, response_code):
    response = pytest.globalDict['response']
    assert_that(response.status_code, equal_to(int(response_code)))


@then('I validate <value> in <path>')
def validate_response_code(base_url, value, path):
    response = pytest.globalDict['response']
    if value != '':
        json_data = json.loads(response.text)
        json_expression = parse(path)
        match = json_expression.find(json_data)
        assert_that(str(match[0].value), contains_string(value))
