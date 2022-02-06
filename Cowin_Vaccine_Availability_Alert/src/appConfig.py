'''
return apllication config dictionary 
'''
import json


def getAppConfigDict(fName="secret/config.json"):
    # load config json into the dictionary
    with open(fName) as f:
        appConf = json.load(f)
        return appConf
