from importlib import import_module


def jsonschema_loader(file: str, jsonschema: str = 'schema'):
    module = import_module(f"schemas.{file}")
    return getattr(module, jsonschema)


def data_loader(file: str, test_data: str = "data"):
    module = import_module(f"data.{file}")
    return getattr(module, test_data)
