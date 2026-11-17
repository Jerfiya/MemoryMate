# 🧠 MemoryMate – AI Chatbot with Conversation Memory

MemoryMate is an AI-powered chatbot built using Python, Streamlit, and Google's Gemini API.

It remembers previous messages within the current session and provides context-aware responses.

## Features

- AI-powered conversations using Google Gemini
- Multi-turn conversation history
- Retains the latest 50 messages as conversation context
- Custom AI personality using a system prompt
- Clear Chat option
- API error handling
- Secure API key management using environment variables

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google Gen AI SDK
- python-dotenv

## Installation

1. Clone this repository.
2. Create a virtual environment:

   `python -m venv .venv`

3. Activate it on Windows:

   `.venv\Scripts\activate`

4. Install dependencies:

   `pip install -r requirements.txt`

5. Create a `.env` file in the project folder and add:

   `GEMINI_API_KEY=your_api_key_here`

6. Run the application:

   `streamlit run app.py`

## Security

Never upload your `.env` file or share your API key publicly.

## Author

Jerfiya J R