import json
from pathlib import Path

import yaml

PARSERS = {
    'json': json.load,
    'yaml': yaml.safe_load,
    'yml': yaml.safe_load,
}


def load_file(file_path):
    path = Path(file_path)
    ext = path.suffix.lower().lstrip('.')

    with path.open() as f:
        return PARSERS[ext](f)