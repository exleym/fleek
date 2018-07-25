from pathlib import Path
import yaml


class Config(object):
    def __init__(self):
        self.templates = []
        self.load()

    @property
    def template(self):
        if len(self.templates) > 0:
            return self.templates[0]
        return None

    def load(self, path=None):
        path = path or self._load_default_path()
        with open(f'{path}/.fleekrc', 'r') as fp:
            txt = fp.read()
        config = yaml.load(txt)
        self._add_templates(config.get('templates', []))

    def _add_templates(self, templates):
        for t in templates:
            self.templates.append(t)

    def _load_default_path(self):
        return str(Path.home())

    def __repr__(self):
        return '<Config(templates=[{}])>'.format(self.templates)
