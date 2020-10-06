from mapping import Mapping

def test_json_mapping():
    mapping = Mapping({}, {"hello": "world"})
    assert mapping.json() == {"mappings": {"dynamic": False, "properties": {"hello": {"type": "text"}}}}

def test_date_mapping():
    mapping = Mapping({}, {"day": "2020-01-01"})
    assert mapping.json() == {"mappings": {"dynamic": False, "properties": {"day": {"type": "date"}}}}

def test_integer_mapping():
    mapping = Mapping({}, {"value": "25"})
    assert mapping.json() == {"mappings": {"dynamic": False, "properties": {"value": {"type": "double"}}}}

def test_config_property_mapping():
    mapping = Mapping({"properties": {"dep": {"type": "keyword"}}}, {"dep": "25"})
    assert mapping.json() == {"mappings": {"dynamic": False, "properties": {"dep": {"type": "keyword"}}}}
