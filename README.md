# terminal-ai-chatbot
A simple chatbot that runs in the terminal, written in Python. It uses the Google Gemini API and remembers the conversation between sessions.

## Features
- Chat with an AI model from the command line
- Conversation history saved to `history.json`, so the bot remembers earlier chats
- `clear` command to reset memory, `quit` to exit
- API key kept in a `.env` file, not in the code
- Handles API errors without crashing

## Demo
<img width="597" height="249" alt="Screenshot 2026-11-14 021613" src="https://github.com/user-attachments/assets/5c10727a-f238-4ac5-963a-f90100377391" />


## How to run
1. Clone the repo:
   ```
   git clone https://github.com/Arsalan470khan/terminal-ai-chatbot.git
   cd terminal-ai-chatbot
   ```
2. Install the requirements:
   ```
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
