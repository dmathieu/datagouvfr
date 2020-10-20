import os
import json

class Config:
    def __init__(self, config):
        self.config = config

    def datasets(self):
        if "datasets" in self.config:
            return self.config["datasets"]
        return []

    def elasticsearch(self):
        if "elasticsearch" in self.config:
            return self.config["elasticsearch"]
        return None

def load():
    with open('config.json') as json_config:
        return Config(json.load(json_config))

def api_key():
    return os.environ['DATA_GOUV_API_KEY']
