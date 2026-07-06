from gendiff.build_diff import build_diff
from tests.conftest import load


def test_build_diff_json():
    first = load('file1.json')
    second = load('file2.json')
    expected = load("expected_diff.json")

    assert build_diff(first, second) == expected


def test_build_diff_yml():
    first = load('file1.yml')
    second = load('file2.yml')
    expected = load("expected_diff.json")

    assert build_diff(first, second) == expected


def test_build_diff_deep_json():
    first = load('file1_deep.json')
    second = load('file2_deep.json')
    expected = load("expected_diff_deep.json")

    assert build_diff(first, second) == expected


def test_build_diff_deep_yml():
    first = load('file1_deep.yml')
    second = load('file2_deep.yml')
    expected = load("expected_diff_deep.json")

    assert build_diff(first, second) == expected