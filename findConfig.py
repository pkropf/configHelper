import os

LOCATIONS=[
    '.',
    os.path.expanduser('~'),
    '/usr/local/etc',
    '/etc',
]

def findConfig(name, locations=LOCATIONS):
    """look for a configuration file in a series of known locations."""

    for l in locations:
        config_path = os.path.join(l, name)
        if os.path.exists(config_path):
            break
    else:
        raise FileNotFoundError(f"{name}, {locations}")

    return config_path
