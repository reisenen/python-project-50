def stylish(diff):
    return '\n'.join(['{', *render_ast(diff), '}'])


def render(node, depth):
    if is_nested_node(node):
        return render_ast(node['children'], depth)
    return render_json(node, depth)


def render_ast(ast, depth=1):
    lines = []

    for key, value in ast.items():
        current_render = get_render(value)
        lines.extend(current_render(depth, key, value))
    return lines


def render_json(json, depth):
    lines = []

    for key, value in json.items():
        lines.extend(render_line(depth, key, value))
    return lines


def get_render(node):
    render_type = node['type']
    return RENDER_TYPES[render_type]


def render_added(depth, key, value):
    return render_line(depth, key, value['value'], '+')


def render_deleted(depth, key, value):
    return render_line(depth, key, value['value'], '-')


def render_unchanged(depth, key, value):
    return render_line(depth, key, value['value'], ' ')


def render_changed(depth, key, value):
    old = render_line(depth, key, value['old'], '-')
    new = render_line(depth, key, value['new'], '+')
    return [*old, *new]


def render_nested(depth, key, node):
    return render_line(depth, key, node)


def render_line(depth, key, value, sign=' '):
    line = []
    indent = render_indent(depth)

    if isinstance(value, dict):
        line.append(f'{indent}{sign} {key}: {{')
        line.extend(render(value, depth + 1))
        line.append(f'{indent}  }}')
    else:
        line.append(f'{indent}{sign} {key}: {render_value(value)}')
    return line


def is_nested_node(node):
    return node.get('type') == 'nested'


def render_indent(depth):
    INDENT_SIZE = 4
    return ' ' * (INDENT_SIZE * depth - 2)


def render_value(value):
    if value is None:
        return 'null'

    if isinstance(value, bool):
        return str(value).lower()

    return str(value)


RENDER_TYPES = {
    'added': render_added,
    'deleted': render_deleted,
    'unchanged': render_unchanged,
    'changed': render_changed,
    'nested': render_nested,
}