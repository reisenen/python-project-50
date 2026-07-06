from tests.conftest import read, diff

from gendiff.formatters.json import json_formatter



def test_json_json():
    assert json_formatter(
        diff('file1_deep.json', 'file2_deep.json')
    ) == read('expected_diff_deep.json')


def test_json_yml():
    assert json_formatter(
        diff('file1_deep.yml', 'file2_deep.yml')
    ) == read('expected_diff_deep.json')
