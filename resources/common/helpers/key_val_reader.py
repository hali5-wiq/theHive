import configparser

class KeyValReader:

    def __init__(self, env_path):
        self.config = configparser.ConfigParser()
        try:
            self.config.read(env_path)
        except FileNotFoundError:
            raise RuntimeError(f"Properties file could not be found at {env_path}")

    def get_property(self, property_name):
        try:
            return self.config.get('DEFAULT', property_name)
        except configparser.NoOptionError:
            raise RuntimeError(f"Cannot return {property_name}")

    def set_property(self, key, value):
        try:
            self.config['DEFAULT'][key] = value
        except Exception:
            raise RuntimeError(f"Not able to set the property (key: {key} and value: {value}")

    def read_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return ""
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return ""