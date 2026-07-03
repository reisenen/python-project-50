def format_dict(items, indent):
    result = []

    for key, value in items.items():
        if isinstance(value, dict):
            result.append(f'{indent}      {key}: {{')
            result.extend(format_dict(value, indent + '    '))
            result.append(f'{indent}      }}')
        else:
            result.append(f'{indent}      {key}: {normalize(value)}')
    return result


def stylish(diff):
    def walk(node, depth):
        output = []
        indent = ' ' * (depth * 2)

        for key, value in node.items():
            if value['type'] == 'added':
                if isinstance(value['value'], dict):
                    output.append(f'{indent}+ {key}: {{')
                    output.extend(format_dict(value['value'], indent))
                    output.append(f'{indent}  }}')
                else:
                    output.append(f'{indent}+ {key}: {normalize(value['value'])}')

            elif value['type'] == 'deleted':
                if isinstance(value['value'], dict):
                    output.append(f'{indent}- {key}: {{')
                    output.extend(format_dict(value['value'], indent))
                    output.append(f'{indent}  }}')
                else:
                    output.append(f'{indent}- {key}: {normalize(value['value'])}')

            elif value['type'] == 'unchanged':
                if isinstance(value['value'], dict):
                    output.append(f'{indent}  {key}: {{')
                    output.extend(format_dict(value['value'], indent))
                    output.append(f'{indent}  }}')
                else:
                    output.append(f'{indent}  {key}: {normalize(value['value'])}')
                
            elif value['type'] == 'changed':
                if isinstance(value['old'], dict):
                    output.append(f'{indent}- {key}: {{')
                    output.extend(format_dict(value['old'], indent))
                    output.append(f'{indent}  }}')
                else:
                    output.append(f'{indent}- {key}: {normalize(value['old'])}')

                if isinstance(value['new'], dict):
                    output.append(f'{indent}+ {key}: {{')
                    output.extend(format_dict(value['new'], indent))
                    output.append(f'{indent}  }}')
                else:
                    output.append(f'{indent}+ {key}: {normalize(value['new'])}')

            else:
                output.append(f'{indent}  {key}: {{')
                output.extend(walk(value['children'], depth + 2))
                output.append(f'{indent}  }}')
    
        return output
    return '\n'.join(['{', *walk(diff, 1), '}'])



def normalize(value):
    if isinstance(value, bool):
        return str(value).lower()
    if not value:
        return 'null'
    return value
