# CHATBOT VERSI RAPIDAPI STREAMLITE

import streamlit as st
import time
import requests

url = "https://chatgpt-best-price.p.rapidapi.com/v1/chat/completions"

headers = {
	"x-rapidapi-key": "6236e2dad0msh715d06b7e3a4db8p1e9719jsnb782d734f7a7",
	"x-rapidapi-host": "chatgpt-best-price.p.rapidapi.com",
	"Content-Type": "application/json"
}

def inputuser(prompt):
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    #print(response.json())

    hasil = response.json()
    output = hasil['choices'][0]['message']['content']
    return output

def response_generator(prompt):
    response = inputuser(prompt)

    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# st.title("Echo Bot")
st.title(":red[Yuda] :blue[.Gpt] 1.0 💬")
# st.title("💬💬💬💬💬")
# st.subheader("💬💬💬💬💬")
# st.header(":red[Yuda] :blue[.Gpt] 1.0")
st.caption("Coba pengalaman _Artificial Intelligence_ :blue[Chatbot AI] dengan mudah :sunglasses:")

# st.subheader("These headers have rotating dividers", divider=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Coba tanyakan apapun di sini...."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator(prompt))
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


