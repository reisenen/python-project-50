from tests.conftest import load

from gendiff.build_diff import build_diff


def test_build_diff():
    first_json = load('file1.json')
    second_json = load('file2.json')

    excepted = load("expected_diff.json")

    assert build_diff(first_json, second_json) == excepted


def test_build_diff_deep():
    first_json = load('file1_deep.json')
    second_json = load('file2_deep.json')

    excepted = load("result_json.json")

    assert build_diff(first_json, second_json) == excepted