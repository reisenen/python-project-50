from tests.conftest import read, diff

from gendiff.formatters.stylish import stylish_formatter



def test_stylish_json():
    assert stylish_formatter(
        diff("file1.json", "file2.json")
    ) == read('result.txt')

    assert stylish_formatter(
        diff("file1_deep.json", "file2_deep.json")
    ) == read('result_deep.txt')


def test_stylish_yml():
    assert stylish_formatter(
        diff("file1.yml", "file2.yml")
    ) == read('result.txt')

    assert stylish_formatter(
        diff("file1_deep.yml", "file2_deep.yml")
    ) == read('result_deep.txt')
