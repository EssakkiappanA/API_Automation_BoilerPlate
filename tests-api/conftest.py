# pylint: disable=invalid-name
# pylint: disable=protected-access
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import

from collections import defaultdict

from common.utils.property_parser import PropertyParser
from common.step_definitions.steps_assertions import *
from common.step_definitions.steps_common import *
from common.utils.env_variables import EnvVariables
from common.page_objects import APIGenerics
from cucumber_tag_expressions import parse


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


def pytest_collection_modifyitems(config, items):
    raw_tags = config.option.tags
    if raw_tags is not None:
        for item in items:
            item_tags = [marker.name for marker in item.own_markers]
            if not parse(raw_tags).evaluate(item_tags):
                item.add_marker(pytest.mark.not_in_scope)


@pytest.fixture(scope='session')
def language(request):
    config = request.config
    language = config.getoption('language')
    if language is not None:
        return language
    return None


@pytest.fixture
def config_parser() -> PropertyParser:
    return PropertyParser()


@pytest.fixture(scope='session')
def project_dir(request, pytestconfig) -> str:
    path_str = request.session.config.known_args_namespace.confcutdir
    return path_str if path_str else str(pytestconfig.rootdir)


@pytest.fixture(scope='session')
def env_variables(project_dir):
    env_vars_file_path = "%s/tests-api/.local.env" % project_dir
    return EnvVariables(env_vars_file_path)


# @pytest.fixture(scope='session')
# def project_data(project_dir):
#     pro_data_file_path = "%s/tests-api/utils/config.properties" % project_dir
#     return ProjectData(pro_data_file_path)


@pytest.fixture
def apigenerics() -> APIGenerics:
    return APIGenerics()
