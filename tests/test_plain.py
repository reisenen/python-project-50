from tests.conftest import load, read

from gendiff.formatters.plain import plain_formatter

from gendiff.build_diff import build_diff



def test_plain_formatted():
    diff_json = build_diff(load('file1_deep.json'), load('file2_deep.json'))
    diff_yaml = build_diff(load('file1_deep.yml'), load('file2_deep.yml'))

    excepted = read('result_plain.txt')

    assert plain_formatter(diff_json) == excepted
    assert plain_formatter(diff_yaml) == excepted