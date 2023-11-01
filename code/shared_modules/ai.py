import openai
import json
from loguru import logger

#Set the openAI key for the whole module
openai.api_key = open('./code/conf/ai.key').readlines()[0]

#Import the AI configuration
with open('./code/conf/ai.conf', 'r') as configFile: aiConfig = json.load(configFile)


def generateStegoText(stegoAlgorithm: str, embeddedText: str, coverContext: str, botName: str, stegoKey: str):
    success: bool = False

    try:
        #Retrieve the configuration based on the selected stego algorithm  
        stegoAlgorithmConfig = [algorithm for algorithm in aiConfig["stegoAlgorithms"] if algorithm["name"] == stegoAlgorithm][0]

        #Prepare a list of messages that will instruct the AI how to embed the embeddedText
        aiModel = stegoAlgorithmConfig["aiModel"] #Retrieving the AI model from the configuration
        aiMessages = [] 

        #Build a list of messages with the messages needed to configure the ai
        for message in stegoAlgorithmConfig["aiMessages"]:
            aiMessages.append({"role": "system", "content": message})

        #Add context for the cover if needed for the algorithm to the messages
        if stegoAlgorithmConfig["askCoverContext"]:
            aiMessages.append({"role": "system", "content": coverContext})

        #Tell the AI to include the name of the bot
            aiMessages.append({"role": "system", "content": "The story you write uses {0} as the main character. It is realy important you name this character in the story".format(botName)})

        #Append the user input to the messages
        aiMessages.append({"role": "user", "content": embeddedText})
        logger.debug("Created messages: {0}".format(aiMessages))

        #Call the API and wait for a reply
        aiChat = openai.ChatCompletion.create(model=aiModel, messages=aiMessages) 
        aiReply = aiChat.choices[0].message.content

        stegoText = aiReply
        success = True
    except Exception as exception:
        logger.error(exception)
        success = False 

    return success, stegoText