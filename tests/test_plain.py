from tests.conftest import read, diff

from gendiff.formatters.plain import plain_formatter



def test_plain_json():
    assert plain_formatter(
        diff('file1_deep.json', 'file2_deep.json')
    ) == read('result_plain.txt')


def test_plain_yml():
    assert plain_formatter(
        diff('file1_deep.yml', 'file2_deep.yml')
    ) == read('result_plain.txt')
