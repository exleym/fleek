from . util import get_config_from_fleekrc

class Blueprint(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Blueprint({self.name})'

    def check_if_default(self):
        default = get_config_from_fleekrc(f'default_blueprints.{self.name}')
        return bool(default)
