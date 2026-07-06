from pathlib import Path

from gendiff.build_diff import build_diff
from gendiff.parser import load_file

TEST_DATA = Path(__file__).parent / "test_data"


def get_path(name):
    return TEST_DATA / name


def read(name):
    return get_path(name).read_text()


def load(name):
    return load_file(get_path(name))


def diff(first, second):
    return build_diff(load(first), load(second))
