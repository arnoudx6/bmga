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
    app.run(debug=True, port=5000)