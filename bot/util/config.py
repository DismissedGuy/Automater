"""
Config class to handle both user-friendly YAML files and JS-friendly JSON files.
Features auto-flushing to disk and changing the config path
TODO: dot notation as alternative to setitem?
"""

import json

import yaml


class ConfigFile(dict):
    def __init__(self, path, config_type='json'):
        self._path = path
        self._config_type = config_type

        with open(path, 'r') as f:
            if config_type == 'json':
                super().__init__(**json.load(f))
            elif config_type == 'yaml':
                super().__init__(**yaml.safe_load(f))
            else:
                raise ValueError(f'Unsupported config type: {type}. Must be one of: json, yaml')

    def __setitem__(self, key, value):
        super().__setitem__(key, value)

        self.flush()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        with open(path, 'r') as f:
            self._path = path
            self.clear()

            if self._config_type == 'json':
                self.update(**json.load(f))
            elif self._config_type == 'yaml':
                self.update(**yaml.safe_load(f))

    def flush(self):
        """Write memory object to disk"""
        with open(self._path, 'w') as f:
            if self._config_type == 'json':
                json.dump(self, f)
            elif self._config_type == 'yaml':
                yaml.safe_dump(self, f)
