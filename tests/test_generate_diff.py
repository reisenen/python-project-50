from tests.conftest import load, read

from gendiff.formatters import get_formatter

from gendiff.build_diff import build_diff

from pytest import fixture



def test_generate_diff_stylish():
    formatter = get_formatter('stylish')

    diff = build_diff(load('file1_deep.json'), load('file2_deep.json'))

    excepted = read('result_deep.txt')

    assert formatter(diff) == excepted


def test_generate_diff_plain():
    formatter = get_formatter('plain')

    diff = build_diff(load('file1_deep.json'), load('file2_deep.json'))

    excepted = read('result_plain.txt')

    assert formatter(diff) == excepted


def test_generate_diff_json():
    formatter = get_formatter('json')

    diff = build_diff(load('file1_deep.json'), load('file2_deep.json'))

    excepted = read('result_json.json')

    assert formatter(diff) == excepted
