from elasticsearch import Elasticsearch, helpers
from time import time
from datetime import datetime

class ES:
    def __init__(self, hosts, index, mapping):
        self.es = Elasticsearch(hosts = hosts)
        self.index = index
        self.mapping = mapping

        self.indices = self.__get_indices()
        self.to_index = []

        self.__setup_template()
        self.most_recent = None

    def add(self, content):
        if self.__exists(content):
            return
        self.to_index.append(content)

    def commit(self):
        return helpers.bulk(self.es, self.__data_to_index())

    def __setup_template(self):
        self.es.indices.put_index_template(name = self.index, body = {
            "index_patterns": [f'{self.index}-*'],
            "template": self.mapping
            })

    def __data_to_index(self):
        for c in self.to_index:
            yield {
                    "_index": self.__indice_for_content(c),
                    "_source": c
                    }
        self.to_index = []

    def __indice_for_content(self, content):
        prop = self.mapping["mappings"]["properties"]
        for v in prop:
            if prop[v]["type"] == "date":
                return f'{self.index}-{content[v]}'
        raise BaseException("No date type found in mapping")

    def __get_indices(self):
        return self.es.indices.get(index = f'{self.index}-*').keys()

    def __exists(self, content):
        return self.__indice_for_content(content) in self.indices
