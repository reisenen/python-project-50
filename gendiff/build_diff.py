def build_diff(first, second):
    keys = first.keys() | second.keys()
    diff = {}

    for key in sorted(keys):
        if key not in first:
            diff[key] = {'type': 'added', 'value': second[key]}
        elif key not in second:
            diff[key] = {'type': 'deleted', 'value': first[key]}
        elif isinstance(first[key], dict) and isinstance(second[key], dict):
            diff[key] = {'type': 'nested', 'children': build_diff(first[key], second[key])}
        elif first[key] == second[key]:
            diff[key] = {'type': 'unchanged', 'value': first[key]}
        else:
            diff[key] = {'type': 'changed', 'old': first[key], 'new': second[key]}

    return diff