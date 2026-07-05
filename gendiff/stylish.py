def stylish(diff):
    return '\n'.join(['{', *render_ast(diff), '}'])


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


def render_nested(depth, key, value):
    return render_line(depth, key, value)


def render_line(depth, key, value, sign=' '):
    line = []
    indent = render_indent(depth)

    prefix = {
    '+': '+ ',
    '-': '- ',
    ' ': '  ',
    }

    if isinstance(value, dict):
        line.append(f'{indent}{prefix[sign]}{key}: {{')
        line.extend(render(value, depth + 1))
        line.append(f'{indent}  }}')
    else:
        line.append(f'{indent}{prefix[sign]}{key}: {render_string(value)}')
    return line


def render(node, depth):
    if 'type' in node and node['type'] == 'nested':
        return render_ast(node['children'], depth)
    return render_json(node, depth)


def render_ast(ast, depth=1):
    render = []

    for key, value in ast.items():
        get_render = dispatch(value)
        render.extend(get_render(depth, key, value))
    return render

 
def render_json(json, depth):
    render = []

    for key, value in json.items():
        render.extend(render_line(depth, key, value))
    return render


def dispatch(node):
    HANDLES = {
        'added': render_added,
        'deleted': render_deleted,
        'unchanged': render_unchanged,
        'changed': render_changed,
        'nested': render_nested,
    }
    node_type = node['type']
    handler = HANDLES[node_type]
    return handler


def render_indent(depth):
    INDENT_SIZE = 4
    return ' ' * (INDENT_SIZE * depth - 2)


def render_string(string):
    if isinstance(string, bool):
        return str(string).lower()
    elif string is None:
        return 'null'
    elif not string:
        return ''
    return string