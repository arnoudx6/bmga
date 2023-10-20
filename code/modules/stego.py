#This will be run when the module is imported
openAIKey = "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"

with open('../../api.key') as file:
    lines = file.readlines()
    print(lines)




def extractEmbeddedTextFromStegoText(stegoText: str, stegoKey):
    success: bool = False
    embeddedText: str = ""

    #Try to retrieve the embeddedText from the stego text
    try:
        embeddedText = "aaa"
        success = True
    except:
        success = False 

    return success, embeddedText

def embedEmbeddedTextInStegoText(embeddedText: str, stegoKey):

    return "bbb"