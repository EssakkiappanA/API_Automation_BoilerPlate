import configparser
import os


class PropertyParser:

    def __init__(self):
        self._config = configparser.RawConfigParser()

    def parser_config_file(self, section, key):
        config_path = os.path.join(os.getcwd(), "tests-api/common/utils/config.properties")
        self._config.read(config_path)
        print(self._config.get(section, key))
        return self._config.get(section, key)
