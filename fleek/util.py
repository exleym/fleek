import yaml
from pathlib import Path


def get_config_from_fleekrc(field=None):
    path = str(Path.home())

    with open(f'{path}/.fleekrc', 'r') as fp:
        txt = fp.read()
    yml = yaml.load(txt)

    if field:
        keys = field.split('.')
        for k in keys:
            yml = yml.get(k, dict())

    return yml or None

