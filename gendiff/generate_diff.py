from gendiff.parser import load_file

from gendiff.stylish import stylish


def generate_diff(file1, file2):
    first_file = load_file(file1)
    second_file = load_file(file2)

    return stylish(get_diff(first_file, second_file))


def get_diff(first, second):
    keys = first.keys() | second.keys()
    diff = {}

    for key in sorted(keys):
        if key not in first:
            diff[key] = {'type': 'added', 'value': second[key]}
        elif key not in second:
            diff[key] = {'type': 'deleted', 'value': first[key]}
        elif isinstance(first[key], dict) and isinstance(second[key], dict):
            diff[key] = {'type': 'nested', 'children': get_diff(first[key], second[key])}
        elif first[key] == second[key]:
            diff[key] = {'type': 'unchanged', 'value': first[key]}
        else:
            diff[key] = {'type': 'changed', 'old': first[key], 'new': second[key]}

    return diff
