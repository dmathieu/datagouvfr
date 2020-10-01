import re

class Parser:
    def __init__(self, headers):
        self.headers = headers

    def parse(self, entry):
        c = {}
        for k,v in enumerate(self.headers):
            c[v] = self.__format(entry[k])
        return c

    def __format(self, value):
        if re.search("^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$", value):
            return re.sub("^([0-9]{2})\/([0-9]{2})\/([0-9]{4})$", "\\3-\\2-\\1", value)
        else:
            return value
