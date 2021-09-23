import logging

import pytest
import re

import requests
from hamcrest import *

logger = logging.getLogger(__name__)


class APIGenerics:

    def __init__(self):
        self._response = ""

    def get_api(self, base_url, endpoint):
        self._response = requests.get(f'{base_url}{endpoint}', verify=False)
        logger.info("response details")
        logger.info(self._response.text)
