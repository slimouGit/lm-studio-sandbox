import requests
import json

API_URL = "http://localhost:1234/v1/chat/completions"

payload = {
    "model": "llama-3.2-1b-instruct",
    "messages": [
        {"role": "system", "content": "Always answer in rhymes. Today is Monday"},
        {"role": "user", "content": "What day is it today?"}
    ],
    "temperature": 0.7,
    "max_tokens": -1,
    "stream": False
}

headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        answer = response_data['choices'][0]['message']['content']
        print("\nAntwort des Modells:\n")
        print(answer)
    else:
        print(f"Fehler: {response.status_code}\n{response.text}")

except requests.exceptions.RequestException as e:
    print(f"Verbindungsfehler: {e}")
