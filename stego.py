def extractEmbeddedTextFromStegoText(stegoText: str, key):
    success: bool = False
    embeddedText: str = ""

    #Try to retrieve the embeddedText from the stego text
    try:
        embeddedText = "aaa"
        success = True
    except:
        success = False 

    return success, embeddedText

def embedEmbeddedTextInStegoText(embeddedText: str, key):
    return "bbb"