import requests
import json

from config import LOCAL_API_URL, SYSTEM_PROMPT

API_URL = LOCAL_API_URL

headers = {
    "Content-Type": "application/json"
}

print("Enter 'exit' to end the conversation.")

while True:
    user_content = input("\nPlease enter your content: ")

    if user_content.lower() == 'exit':
        print("Ending the conversation.")
        break

    payload = {
        "model": "llama-3.2-1b-instruct",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_content}
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