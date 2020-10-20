from elasticsearch import Elasticsearch
from time import time

class ES:
    def __init__(self, hosts, index, mapping):
        self.es = Elasticsearch(hosts = hosts)
        self.index = index
        self.mapping = mapping

        self.pre_indices = list(self.es.indices.get(f'{self.index}-*').keys())
        self.post_indices = []

    def add(self, content):
        indice_name = self.__indice_for_content(content)
        if self.__content_needs_creating(indice_name):
            self.__create_indice(indice_name)
            return self.es.index(index = indice_name, body = content)

    def __create_indice(self, name):
        if not self.__index_exists(name):
            res = self.es.indices.create(index = name, body = self.mapping)
            self.post_indices.append(name)

    def __index_exists(self, name):
        return name in self.pre_indices or name in self.post_indices

    def __content_needs_creating(self, name):
        return name not in self.pre_indices

    def __indice_for_content(self, content):
        prop = self.mapping["mappings"]["properties"]
        for v in self.mapping["mappings"]["properties"]:
            if prop[v]["type"] == "date":
                return f'{self.index}-{content[v]}'
        raise BaseException("No date type found in mapping")
