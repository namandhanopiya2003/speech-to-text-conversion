import yaml
import os

# Loads settings from a YAML file
def load_config(config_path=None):
    if config_path is None:
        # Default path is set to config.yaml inside the same folder
        config_path = os.path.join(os.path.dirname(__file__), "config.yaml")

    # Open the YAML file, read its content, and return it as a Python dictionary
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)
    return config
