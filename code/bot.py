appHeader = """
#####################################################################
### ____  _  _   ___   __     ____  __     __   _  _  ____        ###
###(  _ \( \/ ) / __) / _\   / ___)(  )   / _\ / )( \(  __)       ###
### ) _ (/ \/ \( (_ \/    \  \___ \/ (_/\/    \  \/ / ) _)        ###
###(____/\_)(_/ \___/\_/\_/  (____/\____/\_/\_/ \__/ (____)       ###
###---------------------------------------------------------------###
### A bot for researching hidden botnet communication.            ###
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
waitingForC2 = True
timeBeforeNextC2Poll = 5 #Seconds
processedMessageHashes = []

#Creating an endless loop that contacts the C&C every n seconds
firstLoopItteration = True
while waitingForC2:
    if not firstLoopItteration: #<-- If this is not the first itteration in the loop
        #Anounce sleep
        logger.debug("Waiting {0} seconds before next C2 poll".format(timeBeforeNextC2Poll))
        time.sleep(timeBeforeNextC2Poll)
        
        #Announce new itteration
        logger.debug("New loop itteration")
    else: #<-- If this is the first itteration
        firstLoopItteration = False
        botName = input('Enter the name of this bot: ')

    #Check if there is a new C&C message
    logger.debug("Contacting C2")
    c2Messages = c2Module.get()
    if not c2Messages: #<-- If there is no message from the C&C
        continue #<-- Go to the next loop itteration

    #Filter the messages that are for this botname. 
    filteredC2Messages = c2Module.filterMessagesForMe(c2Messages=c2Messages, botName=botName)
    if not filteredC2Messages:
        logger.debug("No C2 messages for a bot with my name {0}".format(botName))
        continue #<-- Go to the next loop itteration
    else:
        logger.debug("{0} messages for a bot with my name {1}".format(len(filteredC2Messages, botName)))
   
    filteredC2Messages = c2Module.filterUnreadMessages(c2Messages=c2Messages)
    if not filteredC2Messages:
        logger.debug("No messages new C2 messages".format(botName))
        continue #<-- Go to the next loop itteration
    else:
        logger.debug("{0} new messages")

    #Switch to a variable name that is used in the thesis
    stegoTexts = filteredC2Messages

    #Extract the embedded-text from the stego-text
    for stegoText in stegoTexts:


    #Extract the embedded text from the stego text response
    stegoText=c2Messages
    success, embeddedText = stegoModule.extractEmbeddedTextFromStegoText(stegoText=stegoText, stegoKey="bb")
    if not embeddedText or not success:
        continue #<-- Go to the next loop itteration