import json
import os.path

class RegisterService():
    _instance = None

    def __init__(self):
        self.__configPath = "config.json"

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
    
    def LoadConfiguration(self):

        try:
            f = open(self.__configPath)
            self.data = json.load(f)
            f.close()
            print("Config loading success")

        except Exception:
            print("Config file doesnt exist or damaged")

    def GetToken(self):
        return self.data["token"]

    def GetPrefix(self):
        return self.data["prefix"]
    


