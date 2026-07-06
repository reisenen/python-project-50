from tests.conftest import read, diff

from gendiff.formatters.plain import plain_formatter



def test_plain_json():
    current_diff = diff('file1_deep.json', 'file2_deep.json')
    expected = read('expected_plain.txt')

    assert plain_formatter(current_diff) == expected


def test_plain_yml():
    current_diff = diff('file1_deep.yml', 'file2_deep.yml')
    expected = read('expected_plain.txt')

    assert plain_formatter(current_diff) == expected