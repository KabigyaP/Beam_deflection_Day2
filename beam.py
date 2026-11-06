import json

def read_config(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)

        return data

    except FileNotFoundError:
        raise ValueError("Configuration file not found.")

    except json.JSONDecodeError:
        raise ValueError("Invalid JSON configuration file.")