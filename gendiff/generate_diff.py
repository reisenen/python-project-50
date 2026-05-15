import json


def load_file(file):
    with open(file) as f:
        loaded = json.load(f)
    return loaded


def generate_diff(file1, file2):
    first = load_file(file1)
    second = load_file(file2)

    diff = {}

    keys = first.keys() | second.keys()

    for key in sorted(keys):
        if key not in first:
            diff[f'+ {key}'] = second.get(key)
        elif key not in second:
            diff[f'- {key}'] = first.get(key)
        else:
            if first[key] == second[key]:
                diff[f'  {key}'] = first.get(key)
            else:
                diff.update({f'- {key}': first[key], f'+ {key}': second[key]})
    return convert_to_str(diff)


def convert_to_str(coll):
    items = [f'{key}: {normalize_value(value)}' for key, value in coll.items()]
    result = ['{', *items, '}']

    return '\n'.join(result)


def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def format_diff(key, value, char=None):
    MAPPING = {
        '+': f'+ {key}: {value}',
        '-': f'- {key}: {value}',
        'None': f'  {key}: {value}',
    }
    return MAPPING[char](key, value) if char else MAPPING['None'](key, value)
