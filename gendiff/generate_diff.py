import json


def load_file(file):
    with open(file) as f:
        loaded = json.load(f)
    return loaded


def generate_diff(file1, file2):
    first_file = load_file(file1)
    second_file = load_file(file2)

    diff = convert_to_str(get_diff(first_file, second_file))
    return diff


def get_diff(first, second):
    keys = first.keys() | second.keys()
    result = {}

    for key in sorted(keys):
        if key not in first:
            result[get_key(key, '+')] = second[key]
        elif key not in second:
            result[get_key(key, '-')] = first[key]
        elif first[key] == second[key]:
            result[get_key(key)] = first[key]
        else:
            result[get_key(key, '-')] = first[key]
            result[get_key(key, '+')] = second[key]

    return result


def convert_to_str(coll):
    items = [f'{key}: {normalize_value(value)}' for key, value in coll.items()]
    result = ['{', *items, '}']

    return '\n'.join(result)


def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def get_key(key, prefix=None):
    MAPPING = {
        '+': f'+ {key}',
        '-': f'- {key}',
        'None': f'  {key}',
    }
    return MAPPING[prefix] if prefix else MAPPING['None']
