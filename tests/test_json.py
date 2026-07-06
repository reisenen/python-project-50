from tests.conftest import load, read

from gendiff.formatters.json import json_formatter

from gendiff.build_diff import build_diff


def test_json_formatted():
    diff_json = build_diff(load('file1_deep.json'), load('file2_deep.json'))
    diff_yaml = build_diff(load('file1_deep.yml'), load('file2_deep.yml'))

    excepted = read('result_json.json')

    assert json_formatter(diff_json) == excepted
    assert json_formatter(diff_yaml) == excepted