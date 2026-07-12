from tests.conftest import load


def test_json_yaml_parser():
    assert load('file1.json') == load('file1.yml')


def test_json_yaml_parser_deep():
    assert load('file1_deep.json') == load('file1_deep.yml')