import os


def load_env_file():
    dot_env = '.env'
    if 'ENV_FILE' in os.environ:
        dot_env = os.environ['ENV_FILE']
    return dot_env
