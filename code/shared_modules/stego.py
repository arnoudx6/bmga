import shared_modules.ai as aiModule

def extractEmbeddedTextFromStegoText(stegoText: str, stegoKey):
    return "aaa"

def embedEmbeddedTextInStegoText(embeddedText: str, stegoAlgorithm: str, stegoKey):
    success: bool = False

    #Retrieve a stego
    try:
        error, stegoText = aiModule.generateStegoText(stegoAlgorithm="FLR", embeddedText=embeddedText)
        success = True
    except:
        success = False 

    return success, stegoText