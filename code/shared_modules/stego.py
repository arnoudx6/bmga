import shared_modules.ai as aiModule
import json
from loguru import logger

#Make the AI config globaly available
with open('./code/conf/ai.conf', 'r') as configFile: aiConfig = json.load(configFile)

def getValidStegoAlgorithms():
    stegoAlgorithms = [algorithm["name"] for algorithm in aiConfig["stegoAlgorithms"]]
    return stegoAlgorithms

def isCoverContextNeeded(stegoAlgorithm: str):
    contextNeeded = [algorithm["askCoverContext"] for algorithm in aiConfig["stegoAlgorithms"] if algorithm["name"] == stegoAlgorithm][0]
    return contextNeeded

def extractEmbeddedTextFromStegoText(stegoText: str, stegoKey):
    #print(stegoText)
    return True, "aaa"

def embedEmbeddedTextInStegoText(stegoAlgorithm: str, embeddedText: str, coverContext: str, botName: str, stegoKey: str):
    success: bool = False
    #Retrieve a stegoText from the generative ai
    try:
        error, stegoText = aiModule.generateStegoText(stegoAlgorithm=stegoAlgorithm, embeddedText=embeddedText, coverContext=coverContext, botName=botName, stegoKey=stegoKey)
        success = True
    except:
        stegoText = "error"
        success = False 

    return success, stegoText