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
    success: bool = False
    embeddedText: list = []
    #Retrieve a stegoText from the generative ai
    try:
        for line in stegoText.split('.'):
            #First check if we have something to work with
            if not line or line == "":
                continue #<-- Go to the next loop itteration
            #Replace stuff that can harm the extraction but can never contain a hidden text
            line = line.replace('"', '')
            line = line.replace("\n", "")
            line = line.strip()

            #Check if there are any characters left after stripping
            if not line or line == "":
                continue #<-- Go to the next loop itteration

            #Append the first character to the output list
            embeddedText.append(line[0])
        
    except:
        embeddedText = "error"
        success = False 

    return success, embeddedText

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