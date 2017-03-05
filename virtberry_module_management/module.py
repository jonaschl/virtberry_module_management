#!/usr/bin/python3
import pip
import os
import inspect
import importlib
from shutil import copy
import json
import .helper

class virtberry_module:
    def __init__(self, name):
        self.name = name

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
        with open("{0}/{1}.json".format(get_path_module_config(), self.name),"r") as file:
            data = json.load(file)
            new = {}
            new.setdefault(attr, value)
            data.update(new)
            with open("{0}/{1}.json".format(get_path_module_config(), self.name),"w") as file:
                json.dump(data, file, indent=4)

    def get_attributes(self, attr):
        with open("{}".format(self.config_file),"r") as file:
            data = json.load(file)
            return data.get(attr)
