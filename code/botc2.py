appHeader = """
#####################################################################
### ____  _  _   ___   __      ___  ____                          ###
###(  _ \( \/ ) / __) / _\    / __)(___ \                         ###
### ) _ (/ \/ \( (_ \/    \  ( (__  / __/                         ###
###(____/\_)(_/ \___/\_/\_/   \___)(____)                         ###
###---------------------------------------------------------------###
### A bot c2-server for researching hidden botnet communication.  ###
### By using generative AI for creating steganographic stego-text ###
###---------------------------------------------------------------#############################################################
### I, Arnoud Stolk, explicitly declare that I bear no responsibility for the application or misapplication of this project.###
### This project has been developed solely for research purposes.                                                           ###
### The intention behind sharing this source code online is to supplement and support my thesis.                            ###
### Upon completion and evaluation, the thesis will be published on the associated GitHub page.                             ###
### For further information or inquiries, please visit https://github.com/arnoudx6/bmga.                                    ###
###############################################################################################################################
"""

#This is a realy realy simple rest api that is used for command and control.

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for messages
messages = []

@app.route('/messages', methods=['POST'])
def post_message():
    message = request.json.get('message')
    if not message:
        return jsonify({"status": "error", "message": "Message content is required."}), 400

    messages.append(message)
    return jsonify({"status": "success", "message": "Message saved successfully!"}), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify({"messages": messages})

@app.route('/messages/last', methods=['GET'])
def get_last_message():
    if not messages:
        return jsonify({"status": "error", "message": "No messages found."}), 404
    return jsonify({"last_message": messages[-1]})

if __name__ == '__main__':
    app.run(port=5000)