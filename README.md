# terminal-ai-chatbot
A simple chatbot that runs in the terminal, written in Python. It uses the Google Gemini API and remembers the conversation between sessions.

## Features
- Chat with an AI model from the command line
- Conversation history saved to `history.json`, so the bot remembers earlier chats
- `clear` command to reset memory, `quit` to exit
- API key kept in a `.env` file, not in the code
- Handles API errors without crashing

## Demo
<img width="604" height="251" alt="Screenshot 2026-11-14 030846" src="https://github.com/user-attachments/assets/b1b8bda6-e603-4dcd-b7b7-ac793b72533f" />



## How to run
1. Clone the repo:
   ```
   git clone https://github.com/Arsalan470khan/terminal-ai-chatbot.git
   cd terminal-ai-chatbot
   ```
2. Create and activate a virtual environment, then install the requirements:
   ```
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # Mac/Linux
   pip install -r requirements.txt
   ```
3. Get a free API key from [Google AI Studio](https://aistudio.google.com/), then copy `.env.example` to `.env` and paste your key:
   ```
   GEMINI_API_KEY=your_key_here
   ```
4. Run it (replace `chatbot.py` with your file name):
   ```
   python chatbot.py
   ```

## What I learned
- Calling an LLM API with the `requests` library
- Keeping API keys safe with environment variables
- Saving and loading chat history with JSON

## Next
- Add tool use, so the bot can call functions
- Turn it into a small AI agent
