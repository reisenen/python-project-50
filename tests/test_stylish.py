from tests.conftest import load, read

from gendiff.formatters.stylish import stylish_formatter

from gendiff.build_diff import build_diff



def test_stylish_formatted():
    diff_json = build_diff(load('file1.json'), load('file2.json'))
    diff_yaml = build_diff(load('file1.yml'), load('file2.yml'))

    excepted = read('result.txt')

    assert stylish_formatter(diff_json) == excepted
    assert stylish_formatter(diff_yaml) == excepted


def test_stylish_formatted_deep():
    diff_json = build_diff(load('file1_deep.json'), load('file2_deep.json'))
    diff_yaml = build_diff(load('file1_deep.yml'), load('file2_deep.yml'))

    excepted = read('result_deep.txt')

    assert stylish_formatter(diff_json) == excepted
    assert stylish_formatter(diff_yaml) == excepted