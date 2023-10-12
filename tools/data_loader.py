from importlib import import_module


def load_jsonschema(path: str, jsonschema: str = 'schema'):
    module = import_module(f"schemas.{path}")
    return getattr(module, jsonschema)
