# CHATBOT VERSI RAPIDAPI

import requests

url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

headers = {
	"x-rapidapi-key": "6236e2dad0msh715d06b7e3a4db8p1e9719jsnb782d734f7a7",
	"x-rapidapi-host": "chatgpt-best-price.p.rapidapi.com",
	"Content-Type": "application/json"
}

def masukkanprompt(masukprompt):
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": masukprompt
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    #print(response.json())

    hasil = response.json()
    output = hasil['choices'][0]['message']['content']
    return output

while True:
    masukprompt = input("Masukkan pertanyaan disini: ")
    inputuser = masukkanprompt(masukprompt)
    print(inputuser)

    if masukprompt == "exit":
        print("Terima kasih")
        break





