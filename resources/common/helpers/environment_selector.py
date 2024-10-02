import os

class EnvironmentSelector:

    def __init__(self):
        self.env_var = os.environ

    def get_current_env(self):
        environment = self.env_var.get("ENV")
        if environment is None:
            return "sit"
        return environment.lower()