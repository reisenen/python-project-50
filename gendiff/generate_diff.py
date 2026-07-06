from gendiff.parser import load_file

from gendiff.build_diff import build_diff

from gendiff.formatters.stylish import stylish

from gendiff.formatters.plain import plain

from gendiff.formatters.json import json_formatter


def generate_diff(file1, file2, format_name='stylish'):
    first_file = load_file(file1)
    second_file = load_file(file2)

    FORMATTERS = {
        'stylish': stylish,
        'plain': plain,
        'json': json_formatter,
    }

    diff = build_diff(first_file, second_file)

    return FORMATTERS[format_name](diff)
