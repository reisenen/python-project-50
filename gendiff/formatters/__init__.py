from gendiff.formatters.stylish import stylish_formatter

from gendiff.formatters.plain import plain_formatter

from gendiff.formatters.json import json_formatter


FORMATTERS = {
    'stylish': stylish_formatter,
    'plain': plain_formatter,
    'json': json_formatter,
}


def get_formatter(format_name):
    return FORMATTERS[format_name]