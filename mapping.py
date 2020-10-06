import re

class Mapping:
    def __init__(self, config, entry):
        self.config = config
        self.entry = entry

    def json(self):
        return {
            "mappings": {
                "dynamic": False,
                "properties": self.__properties()
            }
        }

    def __properties(self):
        p = {}

        for key in self.entry.keys():
            p[key] = self.__field_property(key)
        return p

    def __field_property(self, key):
        if "properties" in self.config and key in self.config["properties"]:
            return self.config["properties"][key]

        return {
            "type": self.__field_type(key)
        }

    def __field_type(self, key):
        if re.search("^[0-9]+$", self.entry[key]):
            return "double"
        elif re.search("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", self.entry[key]):
            return "date"
        else:
            return "text"
