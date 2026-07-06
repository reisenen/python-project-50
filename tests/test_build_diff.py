from tests.conftest import load, read

from gendiff.build_diff import build_diff


def test_build_diff():
    first_json = load('file1.json')
    second_json = load('file2.json')

    result = read("expected_diff.txt")

    assert build_diff(first_json, second_json) == result