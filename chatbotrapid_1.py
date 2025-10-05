# CHATBOT VERSI RAPIDAPI

import requests

url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

payload = {
	"model": "gpt-4o-mini",
	"messages": [
		{
			"role": "user",
			"content": "siapakah ceo apple?"
		}
	]
}
headers = {
	"x-rapidapi-key": "6236e2dad0msh715d06b7e3a4db8p1e9719jsnb782d734f7a7",
	"x-rapidapi-host": "chatgpt-best-price.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())





