import os
import inspect


_stack = inspect.stack()
_program_path = _stack[-1].filename
_program_dir  = os.path.dirname(_program_path)


LOCATIONS=[
    #look in the same directory as the main program
    _program_dir,

    #look in the etc directory at the same level as the directory of the main program
    os.path.join(_program_dir, '../etc'),

    #look in the currect working directory
    '.',

    #look in the user's home directory
    os.path.expanduser('~'),

    #look in /usr/local/etc
    '/usr/local/etc',

    #look in /etc
    '/etc',
]

print(LOCATIONS)

def findConfig(name, locations=LOCATIONS):
    """look for a configuration file in a series of known locations."""

    for l in locations:
        config_path = os.path.join(l, name)
        if os.path.exists(config_path):
            break
    else:
        raise FileNotFoundError(f"{name}, {locations}")

    return config_path
