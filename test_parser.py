from parser import Parser

def test_parse_entry():
    parser = Parser(["day", "value"])
    assert parser.parse(["2020-01-01", "01"]) == {"day": "2020-01-01", "value": "01"}

def test_parse_entry_invalid_date():
    parser = Parser(["day"])
    assert parser.parse(["01/02/2020"]) == {"day": "2020-02-01"}
