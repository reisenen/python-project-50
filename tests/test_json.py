from gendiff.formatters.json import json_formatter
from tests.conftest import diff, read


def test_json_json():
    current_diff = diff('file1_deep.json', 'file2_deep.json')
    expected = read('expected_diff_deep.json')

    assert json_formatter(current_diff) == expected


def test_json_yml():
    current_diff = diff('file1_deep.yml', 'file2_deep.yml')
    expected = read('expected_diff_deep.json')

    assert json_formatter(current_diff) == expected