from tests.conftest import read, get_path

from gendiff import generate_diff



def test_generate_diff_stylish():
    assert generate_diff(
        get_path('file1_deep.json'), get_path('file2_deep.json'), 'stylish'
    ) == read('expected_stylish_deep.txt')


def test_generate_diff_plain():
    assert generate_diff(
        get_path('file1_deep.json'), get_path('file2_deep.json'), 'plain'
    ) == read('expected_plain.txt')


def test_generate_diff_json():
    assert generate_diff(
        get_path('file1_deep.json'), get_path('file2_deep.json'), 'json'
    ) == read('expected_diff_deep.json')
