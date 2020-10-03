from es import ES
from elasticsearch import Elasticsearch

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

def test_es_add():
    es = ES('datagouvfr_test-add', mapping)
    assert not elastic.indices.exists(index = 'datagouvfr_test-add-2020-01-01')
    res = es.add({"hello": "world", "day": "2020-01-01"})
    assert elastic.indices.exists(index = 'datagouvfr_test-add-2020-01-01')
    assert 'datagouvfr_test-add-2020-01-01' == res['_index']
    assert 'created' == res['result']

def test_add_create_index_with_mapping():
    es = ES('datagouvfr_test-index-mapping', mapping)
    assert not elastic.indices.exists(index = 'datagouvfr_test-index-mapping-2020-01-01')
    es.add({"day": "2020-01-01"})
    assert elastic.indices.exists(index = 'datagouvfr_test-index-mapping-2020-01-01')
    assert mapping['mappings'] == elastic.indices.get(index = 'datagouvfr_test-index-mapping-2020-01-01')['datagouvfr_test-index-mapping-2020-01-01']['mappings']

def test_es_add_preexisting_index():
    elastic.indices.create(index = 'datagouvfr_test-add-preexisting-2020-01-01', body = mapping)
    es = ES('datagouvfr_test-add-preexisting', mapping)
    assert elastic.indices.exists(index = 'datagouvfr_test-add-2020-01-01')
    res = es.add({"day": "2020-01-01"})
    assert None == res
