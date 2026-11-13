import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-flash-lite-latest"   # check Google's docs if this name has changed
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
HISTORY_FILE = "history.json"


def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_history(history):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def ask(history):
    response = requests.post(
        URL,
        headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"},
        json={"contents": history},
        timeout=30,
    )
    response.raise_for_status()
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def main():
    history = load_history()
    print("Chatbot ready. Type 'quit' to exit, 'clear' to reset memory.")
    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "quit":
            break
        if user_input.lower() == "clear":
            history = []
            save_history(history)
            print("Memory cleared.")
            continue
        if not user_input:
            continue

        history.append({"role": "user", "parts": [{"text": user_input}]})
        try:
            reply = ask(history)
        except requests.RequestException as e:
            print(f"API error: {e}")
            history.pop()
            continue

        history.append({"role": "model", "parts": [{"text": reply}]})
        save_history(history)
        print(f"\nBot: {reply}")


if __name__ == "__main__":
    main()