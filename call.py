import requests
import json
import sys
import time


def typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # টাইমিং সেট করুন (0.05 সেকেন্ড ডিলে)


# Phone number processing
typing_effect("Enter phone number:>> ")
phone = input()
phone = phone.lstrip('0')

# Request Captcha Code
url_captcha = 'https://feapi.unicorn88.xyz/api/member/requestCaptchaCode'
captcha_params = {
    'captcha_id': '85a65f94-f722-4887-bc84-ac98a1647b72',
    'captcha_code': '8428'
}

headers_captcha = {
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response_captcha = requests.get(url_captcha, params=captcha_params, headers=headers_captcha)

if response_captcha.status_code == 200:
    print("Captcha request successful.")
else:
    print(f"Failed to request captcha. Status code: {response_captcha.status_code}")
    print(response_captcha.text)

# Request Password Reset
url_reset = 'https://feapi.unicorn88.xyz/api/member/reqFgtPsw'

data_reset = {
    'mobile': phone,
    'prefix': '+880',
    'captcha_id': '85a65f94-f722-4887-bc84-ac98a1647b72',
    'captcha_code': '8428'
}

headers_reset = {
    'content-type': 'application/json',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
}

response_reset = requests.post(url_reset, json=data_reset, headers=headers_reset)

if response_reset.status_code == 200:
    print("Password reset request successful.")
    print(response_reset.json())
else:
    print(f"Failed to request password reset. Status code: {response_reset.status_code}")
    print(response_reset.text)
