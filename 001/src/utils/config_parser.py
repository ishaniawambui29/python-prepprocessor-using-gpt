# config_parser.py
import configparser

class ConfigParser:
    def __init__(self, config_file):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_config(self, section):
        # Retrieve configuration for a specific section
        return dict(self.config.items(section))
