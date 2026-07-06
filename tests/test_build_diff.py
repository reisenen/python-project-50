from tests.conftest import load

from gendiff.build_diff import build_diff


def test_build_diff():
    first_json = load('file1.json')
    second_json = load('file2.json')

    expected = load("expected_diff.json")

    assert build_diff(first_json, second_json) == expected


def test_build_diff_yml():
    first_json = load('file1.yml')
    second_json = load('file2.yml')

    expected = load("expected_diff.json")

    assert build_diff(first_json, second_json) == expected


def test_build_diff_deep():
    first_json = load('file1_deep.json')
    second_json = load('file2_deep.json')

    expected = load("result_json.json")

    assert build_diff(first_json, second_json) == expected


def test_build_diff_deep_yml():
    first_json = load('file1_deep.yml')
    second_json = load('file2_deep.yml')

    expected = load("result_json.json")

    assert build_diff(first_json, second_json) == expected