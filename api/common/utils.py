import importlib


def blueprint_app(module_name: str):
    module, app_name = module_name.split(":")
    return getattr(__import__(module), app_name)
