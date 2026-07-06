def plain_formatter(diff):
    return '\n'.join(render(diff, []))


def render(node, path):
    lines = []

    for key, value in node.items():
        current_render = get_render(value)
        line = current_render(path, key, value)

        if line is None:
            continue

        if isinstance(line, list):
            lines.extend(line)
        else:
            lines.append(line)
    return lines


def get_render(node):
    render_type = node['type']
    return RENDER_TYPES[render_type]


def render_added(path, key, value):
    current_path = path + [key]
    property_name = render_property(current_path)
    current_value = render_value(value['value'])

    line = f"{property_name} was added with value: {current_value}"
    return line


def render_deleted(path, key, value):
    current_path = path + [key]
    property_name = render_property(current_path)

    line = f"{property_name} was removed"
    return line


def render_changed(path, key, value):
    current_path = path + [key]
    property_name = render_property(current_path)
    old_value = render_value(value['old'])
    new_value = render_value(value['new'])

    line = f"{property_name} was updated. From {old_value} to {new_value}"
    return line


def render_unchanged(path, key, value):
    return None


def render_nested(path, key, value):
    current_path = path + [key]

    return render(value['children'], current_path)


def render_property(path):
    current_path = '.'.join(path)

    return f"Property '{current_path}'"


def render_value(value):
    if value is None:
        return 'null'

    if isinstance(value, bool):
        return str(value).lower()

    if isinstance(value, dict):
        return '[complex value]'

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


RENDER_TYPES = {
    'added': render_added,
    'deleted': render_deleted,
    'changed': render_changed,
    'unchanged': render_unchanged,
    'nested': render_nested,
}
