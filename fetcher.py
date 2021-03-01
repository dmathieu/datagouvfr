import requests
import csv
import re

class Fetcher:
    def __init__(self, api_key, dataset):
        self.api_key = api_key
        self.dataset = dataset
        self.data = None
        self.lines = None
        self.load()

    def load(self):
        self.data = requests.get(
                f'https://www.data.gouv.fr/api/1/datasets/{self.dataset["name"]}/',
                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-API-KEY': self.api_key,
                    })

    def len(self):
        return len(self.__lines())

    def header(self):
        reader = csv.reader(self.__lines(), delimiter=self.dataset["delimiter"])
        return next(reader)

    def entries(self):
        reader = csv.reader(self.__lines(), delimiter=self.dataset["delimiter"])
        next(reader)

        for entry in reader:
            yield entry

    def __lines(self):
        if not self.lines:
            self.lines = requests.get(self.__resource()['latest']).text.splitlines()
        return self.lines

    def __resource(self):
        for resource in self.data.json()['resources']:
            if re.search(self.dataset["resource_re"], resource['title']):
                return resource
        return None
