import json


json.dumps()

def json(diff):
    def walk(node):
        output = []

        for key, value in node.items():
            output.append('{')

            if value['type'] == 'added':
                output.extend([f"'type': {value['type']}", f"'key': {key}", f"'new': {value['value']}"])
            
            elif value['type'] == 'deleted':
                output.extend([f"'type': {value['type']}", f"'key': {key}", f"'old': {value['value']}"])
            
            elif value['type'] == 'changed':
                output.extend([f"'type': {value['type']}", f"'key': {key}", f"'new': {value['new']}", f"'old': {value['old']}"])
            
            elif value['type'] == 'nested':
                output.extend([f"'type': {value['type']}", f"'key': {key}", f"'children': {walk(value['children'])}"])
            
            else:
                output.extend([f"'type': {value['type']}", f"'key': {key}", f"'value': {value['value']}"])
            
            output.append('}')
        return output
    
    result = json.dumps(diff)

    return result