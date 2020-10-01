from elasticsearch import Elasticsearch
from time import time

class ES:
    def __init__(self, index):
        self.es = Elasticsearch()
        self.index = index
        self.indice_name = f'{self.index}-{int(time())}'

    def create_indice(self, body = None):
        return self.es.indices.create(index = self.indice_name, body = body)

    def add(self, content):
        return self.es.index(index = self.indice_name, body = content)

    def link_indice(self):
        return self.es.indices.put_alias(name = self.index, index = self.indice_name)

    def clean_indices(self):
        for indice in self.es.indices.get_alias(f'{self.index}-*'):
            if indice != self.indice_name:
                self.es.indices.delete(indice)
