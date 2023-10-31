import openai
import json

#Set the openAI key for the whole module
openai.api_key = open('./code/conf/ai.key').readlines()[0]

#Import the AI configuration
with open('./code/conf/ai.conf', 'r') as configFile: aiConfig = json.load(configFile)


def generateStegoText(stegoAlgorithm: str, embeddedText: str):
    success: bool = False

    try:
        #Retrieve the configuration based on the selected stego algorithm
        stegoAlgorithmConfig = [algorithm for algorithm in aiConfig["stegoAlgorithms"] if algorithm["name"] == stegoAlgorithm][0]

        #Prepare a list of messages that will instruct the AI how to embed the embeddedText
        aiModel = stegoAlgorithmConfig["aiModel"] #Retrieving the AI model from the configuration
        aiMessages = [json.loads(stegoAlgorithmConfig["aiMessages"][0])] #Abusing the json library to covert a string dict into a dict :)
        aiMessages.append({"role": "user", "content": "{0}".format(embeddedText)})

        #Call the API and wait for a reply
        aiChat = openai.ChatCompletion.create(model=aiModel, messages=aiMessages) 
        aiReply = aiChat.choices[0].message.content

        stegoText = aiReply
        success = True
    except:
        success = False 

    return success, stegoText