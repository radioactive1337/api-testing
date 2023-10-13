from importlib import import_module


def jsonschema_loader(path: str, jsonschema: str = 'schema'):
    module = import_module(f"schemas.{path}")
    return getattr(module, jsonschema)


def data_loader(path: str, test_data: str = "data"):
    module = import_module(f"data.{path}")
    return getattr(module, test_data)
