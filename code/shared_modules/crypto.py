import hashlib

def getMessageHash(message: str):
    messageHash = hashlib.sha1(bytes(message, encoding="utf8")).hexdigest() #For now using sha1 because of the speed.
    return messageHash