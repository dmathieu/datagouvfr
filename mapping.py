import re

class Mapping:
    def __init__(self, entry):
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
            p[key] = {
                "type": self.__field_type(key, self.entry[key])
            }
        return p

    def __field_type(self, key, value):
        if key == "dep": # TODO: REMOVE HACK. But not all departements are integers
            return "text"
        elif re.search("^[0-9]+$", value):
            return "double"
        elif re.search("^[0-9]{4}-[0-9]{2}-[0-9]{2}$", value):
            return "date"
        else:
            return "text"
