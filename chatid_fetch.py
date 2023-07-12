import requests

def get_chat_id(api_token):
    url = f"https://api.telegram.org/bot{api_token}/getUpdates"
    response = requests.get(url)
    data = response.json()
    chat_id = data["result"][0]["message"]["chat"]["id"]
    return chat_id

# Replace <YOUR_API_TOKEN> with your actual API token
api_token = "<API TOKEN>"
chat_id = get_chat_id(api_token)
print("Chat ID:", chat_id)
