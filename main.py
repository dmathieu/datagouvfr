import os
import es
import config
from tqdm import tqdm

from fetcher import Fetcher
from parser import Parser
from mapping import Mapping

def first_entry(fetcher):
    return next(fetcher.entries())

if __name__ == "__main__":
    for dataset in config.load():
        print(f'Indexing Dataset {dataset["name"]}')

        fetcher = Fetcher(
                config.api_key(),
                dataset["name"],
                dataset["resource_re"]
                )
        parser = Parser(fetcher.header())
        mapping = Mapping(parser.parse(first_entry(fetcher)))

        db = es.ES(dataset["index"])
        db.create_indice(body = mapping.json())

        with tqdm(total = fetcher.len()) as t:
            for entry in fetcher.entries():
                db.add(parser.parse(entry))
                t.update()

        db.link_indice()
        db.clean_indices()
