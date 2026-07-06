from tests.conftest import read, diff

from gendiff.formatters.stylish import stylish_formatter



def test_stylish_json():
    current_diff = diff('file1.json', 'file2.json')
    expected = read('expected_stylish.txt')

    assert stylish_formatter(current_diff) == expected


def test_stylish_yml():
    current_diff = diff('file1.yml', 'file2.yml')
    expected = read('expected_stylish.txt')

    assert stylish_formatter(current_diff) == expected


def test_stylish_deep_json():
    current_diff = diff('file1_deep.json', 'file2_deep.json')
    expected = read('expected_stylish_deep.txt')

    assert stylish_formatter(current_diff) == expected


def test_stylish_deep_yml():
    current_diff = diff('file1_deep.yml', 'file2_deep.yml')
    expected = read('expected_stylish_deep.txt')

    assert stylish_formatter(current_diff) == expected