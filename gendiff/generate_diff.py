from gendiff.parser import load_file


def generate_diff(file1, file2):
    first_file = load_file(file1)
    second_file = load_file(file2)

    return render_diff(get_diff(first_file, second_file))


def get_diff(first, second):
    keys = first.keys() | second.keys()
    diff = {}

    for key in sorted(keys):
        if key not in first:
            diff[key] = {'added': second[key]}
        elif key not in second:
            diff[key] = {'deleted': first[key]}
        elif first[key] == second[key]:
            diff[key] = {'unchanged': first[key]}
        else:
            diff[key] = {'changed': {'old': first[key], 'new': second[key]}}

    return diff


def render_diff(diff):
    output = {}

    for key, value in diff.items():
        if 'added' in value:
            output[f'+ {key}'] = value['added']
        elif 'deleted' in value:
            output[f'- {key}'] = value['deleted']
        elif 'unchanged' in value:
            output[f'  {key}'] = value['unchanged']
        elif 'changed' in value:
            output[f'- {key}'] = value['changed']['old']
            output[f'+ {key}'] = value['changed']['new']

    return convert_to_text(output)


def convert_to_text(coll):
    items = [
        f'  {key}: {normalize_value(value)}' for key, value in coll.items()
    ]
    result = ['{', *items, '}']

    return '\n'.join(result)


def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value