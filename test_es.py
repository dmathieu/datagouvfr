from es import ES
from elasticsearch import Elasticsearch
import time

elastic = Elasticsearch()
mapping = {
    "mappings": {
        "properties": {
            "day": { "type": "date" }
        }
    }
}

def teardown_module(module):
    elastic.indices.delete('datagouvfr_test-*')
    elastic.indices.delete_index_template('datagouvfr_test-*')

def test_es_add():
    es = ES(None, 'datagouvfr_test-add', mapping)
    assert not elastic.indices.exists(index = 'datagouvfr_test-add-2020-01-01')
    es.add({"hello": "world", "day": "2020-01-01"})
    es.commit()
    assert elastic.indices.exists(index = 'datagouvfr_test-add-2020-01-01')
    time.sleep(1)
    data = elastic.search(index = 'datagouvfr_test-add-2020-01-01')
    assert len(data['hits']['hits']) == 1

def test_add_create_index_with_mapping():
    es = ES(None, 'datagouvfr_test-index-mapping', mapping)
    assert not elastic.indices.exists(index = 'datagouvfr_test-index-mapping-2020-01-01')
    es.add({"day": "2020-01-01"})
    es.commit()
    assert elastic.indices.exists(index = 'datagouvfr_test-index-mapping-2020-01-01')
    assert mapping['mappings'] == elastic.indices.get(index = 'datagouvfr_test-index-mapping-2020-01-01')['datagouvfr_test-index-mapping-2020-01-01']['mappings']
