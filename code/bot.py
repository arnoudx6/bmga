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

#Import custom modules
import modules.c2 as c2Module
import modules.stego as stegoModule

#Initialize script variables
waitingForC2 = True
timeBeforeNextC2Poll = 5
lastMessageCounter = 0

#Creating an endless loop that contacts the C&C every n seconds
firstLoopItteration = True
while waitingForC2:
    if not firstLoopItteration: #<-- If this is not the first itteration in the loop
        #Anounce sleep
        print("Waiting {0} seconds before next C2 poll".format(timeBeforeNextC2Poll))
        time.sleep(timeBeforeNextC2Poll)
        
        #Announce new itteration
        print("New loop itteration")
    else: #<-- If this is the first itteration
        firstLoopItteration = False

    #Check if there is a new C&C message
    print("Contacting C2")
    c2Response = c2Module.get()
    if not c2Response: #<-- If there is no message from the C&C
        continue #<-- Go to the next loop itteration

    #Extract the embedded text from the stego text response
    success, embeddedText = stegoModule.extractEmbeddedTextFromStegoText("aa", "bb")
    if (not embeddedText) or (not success):
        continue #<-- Go to the next loop itteration


    #Print the serialized text
    print("{0}|Message from Master: {1}".format(time.gmtime, serializedText))