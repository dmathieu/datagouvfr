import config

def test_config_load():
    c = config.load()
    assert type(c) is config.Config
