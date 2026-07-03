def plain(diff):

    def walk(node, path):
        output = []
        current_path = path

        for key, value in node.items():
            current_path.append(key)

            if value['type'] == 'nested':
                output.extend(walk(value['children'], current_path))

            elif value['type'] == 'added':
                if isinstance(value['value'], dict):
                    output.append(f"Property '{'.'.join(current_path)}' was added with value: [complex value]")
                else:
                    output.append(f"Property '{'.'.join(current_path)}' was added with value: {normalize(value['value'])}")
            
            elif value['type'] == 'changed':
                if isinstance(value['old'], dict):
                    output.append(f"Property '{'.'.join(current_path)}' was updated. From [complex value] to {normalize(value['new'])}")
                elif isinstance(value['new'], dict):
                    output.append(f"Property '{'.'.join(current_path)}' was updated. From {normalize(value['old'])} to [complex value]")
                else:
                    output.append(f"Property '{'.'.join(current_path)}' was updated. From {normalize(value['old'])} to {normalize(value['new'])}")
            
            elif value['type'] == 'deleted':
                output.append(f"Property '{'.'.join(current_path)}' was removed")
            current_path.pop()
        return output

    return '\n'.join(walk(diff, []))


def normalize(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if not value:
        return f"''"
    return f"'{value}'"