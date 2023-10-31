with open('../openai.key') as file:
    lines = file.readlines()
    key = lines[0]

import openai

openai.api_key = key
messages = [ {"role": "system", "content": 
			"Je bent een systeem dat tekst tussen twee zinnen plakt. De twee zinnen mag je zelf bedenken, maar de tekst er tussen moet letterlijk overgenomen worden."} ] 
while True: 
	message = input("User : ") 
	if message: 
		messages.append( 
			{"role": "user", "content": message}, 
		) 
		chat = openai.ChatCompletion.create( 
			model="gpt-3.5-turbo", messages=messages 
		) 
	reply = chat.choices[0].message.content 
	print(f"ChatGPT: {reply}") 
	messages.append({"role": "assistant", "content": reply}) 
