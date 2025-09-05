import streamlit as st
import requests
import os


API_KEY = 'sk-53751d5c6f344a5dbc0571de9f51313e'
API_URL = 'https://api.deepseek.com/v1/chat/completions'


def enviar_mensaje(mensaje, modelo='deepseek-chat'):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": modelo,
        "messages": st.session_state.messages
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f" Error al llamar la API: {str(e)}"

def main():
    st.title("Chatbot con DeepSeek y Streamlit")

  if 'messages' not in st.session_state:
        st.session_state.messages = [
           {
            "role": "system",
            "content": """Eres Bugs Bunny, el famoso personaje animado. Responde con humor, usa frases icónicas como '¿Qué hay de nuevo, viejo?' y mantén una actitud relajada y divert>
          }
        ]


for message in st.session_state.messages:
        if message["role"] != "system":  
            with st.chat_message(message["role"]):
                st.markdown(message["content"])


    if prompt := st.chat_input("Escribe tu mensaje..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        if prompt.lower() == "salir":
            respuesta = "¡Hasta luego!"
        else:
            respuesta = enviar_mensaje(prompt)

        with st.chat_message("assistant"):
            st.markdown(respuesta)
        st.session_state.messages.append({"role": "assistant", "content": respuesta})


if __name__ == "__main__":
    main()
