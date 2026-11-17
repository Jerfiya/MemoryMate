import streamlit as st
import os
from dotenv import load_dotenv
from google import genai
# Load API key from .env file
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

# Connect to Gemini
client = genai.Client(api_key=API_KEY)
if not API_KEY:
    st.error("Gemini API key not found. Please check your .env file.")
    st.stop()
    # Page configuration
st.set_page_config(
    page_title="MemoryMate",
    page_icon="🧠"
)

# Chatbot title
st.title("🧠 MemoryMate")

st.write("Your AI chatbot that remembers conversations!")

st.caption("Powered by Google Gemini")
# Clear conversation history
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# Get user input
user_input = st.chat_input("Ask MemoryMate anything...")
if user_input:
    # Save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
        # Generate Gemini response
    try:
        chat_history = []

        for msg in st.session_state.messages[-50:]:
            role = "model" if msg["role"] == "assistant" else "user"

            chat_history.append({
                "role": role,
                "parts": [{"text": msg["content"]}]
            })

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=chat_history,
            config={
                "system_instruction": """
You are MemoryMate, a friendly and intelligent AI assistant.

Your responsibilities:
1. Remember details from the current conversation.
2. Give clear and easy-to-understand answers.
3. Explain difficult topics step by step.
4. Be supportive, polite and conversational.
5. Avoid unnecessarily long answers.
6. Never pretend to remember information that was not provided.
"""
            }
        )

        bot_reply = response.text

        # Save AI response
        st.session_state.messages.append({
            "role": "assistant",
            "content": bot_reply
        })

        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(bot_reply)

    except Exception as e:
        st.error(f"Something went wrong: {e}")
