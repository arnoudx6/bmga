import shared_modules.ai as aiModule
import json

def getValidStegoAlgorithms():
    with open('./code/conf/ai.conf', 'r') as configFile: aiConfig = json.load(configFile)
    stegoAlgorithms = [algorithm["name"] for algorithm in aiConfig["stegoAlgorithms"]]
    return stegoAlgorithms

def extractEmbeddedTextFromStegoText(stegoText: str, stegoKey):
    return "aaa"

def embedEmbeddedTextInStegoText(embeddedText: str, stegoAlgorithm: str, stegoKey):
    success: bool = False

    #Retrieve a stego
    try:
        error, stegoText = aiModule.generateStegoText(stegoAlgorithm=stegoAlgorithm, embeddedText=embeddedText)
        success = True
    except:
        success = False 

    return success, stegoText