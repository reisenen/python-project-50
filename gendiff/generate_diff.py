import json


def generate_diff(first, second):
    first = json.load(open(first))
    second = json.load(open(second))
    diff = {}

    keys = first.keys() | second.keys()

    for key in sorted(keys):
        if key not in first:
            diff[f'+ {key}'] = second.get(key)
        elif key not in second:
            diff[f'- {key}'] = first.get(key)
        else:
            if first[key] == second[key]:
                diff[key] = first.get(key)
            else:
                diff.update({f'- {key}': first[key], f'+ {key}': second[key]})
    return transform_to_str(diff)


def transform_to_str(data):
    result = []
    for k, v in data.items():
        result.append(f'{k}: {v}')
    string = '\n'.join(result)
    return '{' + '\n' + string + '\n' + '}'