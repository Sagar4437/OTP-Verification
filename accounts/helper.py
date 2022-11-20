import random
from django.conf import settings
import requests





def send_otp_to_phone_number(phone_number):
    try:
        otp = random.randint(1000,9999)
        url = f"https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}"
        response = requests.get(url)
        return otp
    except Exception as e:
        print(e)
        return None

def verify_otp(otp_input,session_id):
    try:
        url = f"https://2factor.in/API/V1/{settings.API_KEY}/SMS/VERIFY/{session_id}/{otp_input}"
        response = requests.get(url)
        print(response.status_code)
        return response.status_code==400

    except Exception as e:
        return False

