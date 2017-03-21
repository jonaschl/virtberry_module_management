#!/usr/bin/python3
import pip
import os
import inspect
import importlib
from shutil import copy
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

class virtberry_module:
    def __init__(self, name):
        self.name = name
        self.config_file = "{0}/{1}.json".format(get_path_module_config(), self.name)

    def install(self, path):
        pip.main(['install', path])
        print(get_path_from_module_name(self.name))
        # install configuration file
        # get path for module configuration files
        dst = get_path_module_config()
        copy("{}/config/sample-config.json".format(get_path_from_module_name(self.name)), "{0}/{1}.json".format(dst, self.name))

    def enable(self):
        self.set_attributes("status", "enabled")

    def disable(self):
        self.set_attributes("status", "disabled")

    def set_attributes(self, attr, value):
        with open(self.config_file,"r") as file:
            data = json.load(file)
            new = {}
            new.setdefault(attr, value)
            data.update(new)
            with open(self.config_file,"w") as file:
                json.dump(data, file, indent=4)

    def get_attributes(self, attr):
        with open(self.config_file,"r") as file:
            data = json.load(file)
            return data.get(attr)
