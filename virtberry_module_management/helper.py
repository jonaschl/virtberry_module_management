#!/usr/bin/python3
import os
import inspect
import importlib
import json

PathToNormalConfigFile = "/etc/virtberry/config.json"

def import_module_from_name(name):
    return importlib.import_module("{}".format(name))

def get_object_from_name(module, name):
    return getattr(module, name)

def get_path_from_module_name(name):
    return os.path.dirname(os.path.abspath(inspect.getfile(import_module_from_name(name))))

def get_path_module_config():
    with open(PathToNormalConfigFile,"r") as file:
        data = json.load(file)
        return data["path_module_config"]

def get_enabled_modules():
    enabled_modules = []
    for entry in os.scandir("{}/".format(get_path_module_config())):
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith(".json"):
            name = entry.name.replace(".json","")
            print(os.path.abspath(entry.name))
            module = virtberry_module(name)
            if module.get_attributes("status") == "enabled":
                enabled_modules.append(name)
    return enabled_modules
