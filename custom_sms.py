import requests
import sys
import time


def typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # টাইমিং সেট করুন (0.05 সেকেন্ড ডিলে)



typing_effect("Enter number:>> ")
phone = input()

typing_effect("Enter message:>> ")
text = input()


# API URL
url = "http://bulksmsbd.net/api/smsapi"

# Parameters
params = {
    "api_key": "dxL6s1sQb0J2jyusJU6l",
    "type": "text",
    "number": phone,  # Replace with the actual phone number
    "senderid": "8809617614409",
    "message": text,
}

try:
    # Sending the request
    response = requests.get(url, params=params)
    
    # Check response status
    if response.status_code == 200:
        print("SMS sent successfully!")
        print("Response:", response.text)
    else:
        print("Failed to send SMS.")
        print("Response Code:", response.status_code)
        print("Response:", response.text)
except Exception as e:
    print("An error occurred:", str(e))
