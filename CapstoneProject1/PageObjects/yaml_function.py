# yaml_function

from yaml import load
from yaml.loader import SafeLoader


class YAML_Function:
    def __init__(self, file_name):
        self.file = file_name

    # read the Yaml file
    def yaml_reader(self):
        with open(self.file) as file:
            data = load(file, Loader=SafeLoader)
        return data
