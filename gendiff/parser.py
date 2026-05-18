import json
import yaml


def load_file(file):
    _, ext = str(file).split('.')

    with open(file) as f:
        if ext in ('yml', 'yaml'):
            loaded = yaml.safe_load(f)
        if ext in ('json'):
            loaded = json.load(f)
    return loaded