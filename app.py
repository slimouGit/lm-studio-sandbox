import requests
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

from config import LOCAL_API_URL, MODEL

API_URL = LOCAL_API_URL

headers = {
    "Content-Type": "application/json"
}

print("Enter 'exit' to end the conversation.")

language_map = {
    'en': 'English',
    'de': 'German',
    'es': 'Spanish'
}
language_code = input("Please select the language (en/de/es): ").strip().lower()
language = language_map.get(language_code, 'English')
print(language)

SYSTEM_PROMPT = ("You are a friendly and casual conversation partner helping the user improve their " + language + ". "
                 "Keep the tone light and relaxed. Analyze the user's input for spelling and phrasing, "
                 "and suggest improvements when needed. Always continue the conversation naturally.")
ADDITIONAL_PROMPT = ("Please check the user's input for spelling and phrasing, correct it, "
                     "and continue the conversation in a friendly manner, in the selected language.")


while True:
    user_content = input("\nPlease enter your content: ")

    if user_content.lower() == 'exit':
        print("Ending the conversation.")
        break

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content + ADDITIONAL_PROMPT}
        ],
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }

    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            response_data = response.json()
            answer = response_data['choices'][0]['message']['content']
            print("\nModel's response:\n")
            print(answer)
        else:
            print(f"Error: {response.status_code}\n{response.text}")

    except requests.exceptions.RequestException as e:
        print(f"Connection error: {e}")