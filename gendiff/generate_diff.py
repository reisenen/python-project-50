from gendiff.build_diff import build_diff
from gendiff.formatters import get_formatter
from gendiff.parser import load_file


def generate_diff(file1, file2, format_name='stylish'):
    first = load_file(file1)
    second = load_file(file2)

    diff = build_diff(first, second)

    formatter = get_formatter(format_name)

    return formatter(diff)
