import requests
import time

# Telegram Bot API credentials
bot_token = 'YOUR_BOT_TOKEN'
chat_id = 'YOUR_CHAT_ID'

# List of servers to check
servers = [
    {'name': 'Server 1', 'url': 'http://server1.com'},
    {'name': 'Server 2', 'url': 'http://server2.com'},
    {'name': 'Server 3', 'url': 'http://server3.com'}
]


# Function to send Telegram message
def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("Telegram message sent successfully!")
    else:
        print("Failed to send Telegram message. Response:", response.text)


# Check server status
def check_server_status(server):
    server_name = server['name']
    server_url = server['url']
    try:
        response = requests.get(server_url)
        if response.status_code == 200:
            print(f"{server_name} is up and running!")
        else:
            send_telegram_message(f"{server_name} is down! Response code: {response.status_code}")
    except requests.ConnectionError:
        send_telegram_message(f"{server_name} is down!")


# Main program
if __name__ == '__main__':
    while True:
        for server in servers:
            check_server_status(server)
            time.sleep(1)  # Delay for 1 second between pings

        time.sleep(60)  # Delay for 60 seconds before rechecking all servers
