import json
from pathlib import Path

import yaml

PARSERS = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def load_file(file_path):
    ext = Path(file_path).suffix.lower().lstrip('.')

    with open(file_path) as f:
        return PARSERS[ext](f)