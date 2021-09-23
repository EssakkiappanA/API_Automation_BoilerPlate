# pylint: disable=invalid-name
# pylint: disable=protected-access
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

from collections import defaultdict

from common.step_definitions.steps_assertions import *
from common.step_definitions.steps_common import *
from utils.env_variables import EnvVariables
from common.page_objects.api_generics import APIGenerics


def pytest_configure(config):
    config.option.keyword = 'automated'
    config.option.markexpr = 'not not_in_scope'
    pytest.globalDict = defaultdict()


def pytest_addoption(parser):
    parser.addoption('--language',
                     action='store',
                     default='en',
                     type=str,
                     help='Application language')
    parser.addoption('--tags',
                     metavar="str",
                     help='Will filter tests by given tags')


@pytest.fixture(scope='session')
def language(request):
    config = request.config
    language = config.getoption('language')
    if language is not None:
        return language
    return None


@pytest.fixture(scope='session')
def env_variables(request):
    env_vars_file_path = "%s/.local.env" % request.session.config.known_args_namespace.confcutdir
    return EnvVariables(env_vars_file_path)


@pytest.fixture
def apigenerics() -> APIGenerics:
    return APIGenerics()

