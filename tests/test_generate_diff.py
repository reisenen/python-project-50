from gendiff import generate_diff
from tests.conftest import get_path, read


def test_generate_diff_stylish():
    assert generate_diff(
        file1=get_path('file1_deep.json'), 
        file2=get_path('file2_deep.json'), 
        format_name='stylish'
    ) == read('expected_stylish_deep.txt')


def test_generate_diff_plain():
    assert generate_diff(
        file1=get_path('file1_deep.json'), 
        file2=get_path('file2_deep.json'), 
        format_name='plain'
    ) == read('expected_plain.txt')


def test_generate_diff_json():
    assert generate_diff(
        file1=get_path('file1_deep.json'), 
        file2=get_path('file2_deep.json'), 
        format_name='json'
    ) == read('expected_diff_deep.json')