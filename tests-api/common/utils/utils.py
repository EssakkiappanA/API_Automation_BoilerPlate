# pylint: disable=import-outside-toplevel
# pylint: disable=no-member
import configparser
import errno
import json
import math
import os
from os import path, strerror
from pathlib import Path

import pytest


class Utils:

    def __init__(self):
        pass

    def get_env_name(caps: dict):
        os = caps['os'] if 'os' in caps else None
        os_version = caps['os_version'] if 'os_version' in caps else ''
        env = caps['browser'] if 'browser' in caps else caps['device'] if 'device' in caps else 'Chrome'

        if os is None:
            env_name = '%s - %s' % (env, os_version)
        else:
            env_name = '%s %s - %s' % (os, os_version, env)
        print('Test results will be exported to "%s" TestRail Configuration' % env_name)
        return env_name

    def read_file(self,file_name):
        # file_path = re.sub(r'utils.(\w+)', file_name, path.abspath(__file__))
        file_path = get_file_path(file_name)
        with open(file_path, encoding="utf-8") as fl:
            extension = path.splitext(file_path)[1]
            if extension == '.json':
                raw_data = json.load(fl)
                return raw_data
            if extension == '.txt':
                raw_data = fl.read()
                return raw_data
            raise extension

    def get_file_path(file_name):
        path_object = Path(file_name)
        if not path_object.exists():
            raise FileNotFoundError(errno.ENOENT, strerror(errno.ENOENT), file_name)
        return path_object.resolve()

    def get_horizontal_spacing(elem_1, elem_2):
        spacing = 0  # TODO

        return spacing

    def get_vertical_spacing(elem_1, elem_2):
        spacing = 0  # TODO

        return spacing

    def round_down(self, n, decimals=0):
        multiplier = 10 ** decimals
        return math.floor(n * multiplier) / multiplier

    def read_property_data(self):
        config = configparser.RawConfigParser()
        config.read('../../common/utils/config.properties')
        print(config.sections())
        # print(config.get('reqresDetails','base_url'))
