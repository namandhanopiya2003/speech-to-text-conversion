import yaml
import os

# It opens the config.yaml file and turns its content into a Python readable dictionary
def load_config(config_path=None):
    if config_path is None:
        
        # If no path is given, it uses the default "config.yaml"
        config_path = os.path.join(os.path.dirname(__file__), "config.yaml")

    # It opens the config.yaml file and read its content
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)             # Converts the YAML content into a Python dictionary (key-value pairs)
        
    return config
