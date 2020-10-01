import os
import json

def load():
    with open('config.json') as json_config:
        return json.load(json_config)

def api_key():
    return os.environ['DATA_GOUV_API_KEY']
