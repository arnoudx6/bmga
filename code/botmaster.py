#####################################################################
### ____  _  _   ___   __     ____   __  ____                     ###
###(  _ \( \/ ) / __) / _\   (  _ \ /  \(_  _)                    ###
### ) _ (/ \/ \( (_ \/    \   ) _ ((  O ) )(                      ###
###(____/\_)(_/ \___/\_/\_/  (____/ \__/ (__)                     ###
###---------------------------------------------------------------###
### A bot for researching hidden botnet communication...          ###
### By using generative AI for creating steganographic stego text ###
###---------------------------------------------------------------###########################################################
### I, Arnoud Stolk, explicitly declare that I bear no responsibility for the application or misapplication of this project.#
### This project has been developed solely for research purposes.                                                           #
### The intention behind sharing this source code online is to supplement and support my thesis.                            #
### Upon completion and evaluation, the thesis will be published on the associated GitHub page.                             #
### For further information or inquiries, please visit https://github.com/arnoudx6/bmga.                                    #
#############################################################################################################################

#Import standard modules
import time
import openai

#Import custom modules
import modules.c2 as c2Module
import modules.stego as stegoModule
import modules.compression as compressionModule
import modules.crypto as cryptoModModule

#Initialize script variables
waitingForC2ToSend = True

while waitingForC2ToSend:
    #
    dataToSend = input("Input ....")

    #Serialize the input
    serializedText = dataToSend

    #Compress the input to make the data smaller to send
    compressedText = compressionModule.compress(serializedText)

    #Use steganography to embed the embedded text into the stego text
    embeddedText = compressedText
    stegoText = stegoModule.embedEmbeddedTextInStegoText(embeddedText, "bbb")

    #Push the stego text to the C&C
    c2Module.push()

