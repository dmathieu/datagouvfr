from elasticsearch import Elasticsearch
from time import time

class ES:
    def __init__(self, index, mapping):
        self.es = Elasticsearch()
        self.index = index
        self.mapping = mapping
        self.indices = list(self.es.indices.get(f'{self.index}-*').keys())

    def add(self, content):
        indice_name = self.__indice_for_content(content)
        self.__create_indice(indice_name)
        return self.es.index(index = indice_name, body = content)

    def __create_indice(self, name):
        if name not in self.indices:
            res = self.es.indices.create(index = name, body = self.mapping)
            self.indices.append(name)

    def __indice_for_content(self, content):
        prop = self.mapping["mappings"]["properties"]
        for v in self.mapping["mappings"]["properties"]:
            if prop[v]["type"] == "date":
                return f'{self.index}-{content[v]}'
        raise Error("No date type found in mapping")
