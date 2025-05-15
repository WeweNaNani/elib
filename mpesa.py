import base64
import datetime
import requests
from config import *

def get_access_token():
    url = f"{MPESA_BASE_URL}/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(url, auth=(MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET))
    return response.json().get('access_token')

def generate_password():
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    data = MPESA_SHORTCODE + MPESA_PASSKEY + timestamp
    password = base64.b64encode(data.encode()).decode()
    return password, timestamp

def initiate_stk_push(amount, phone_number, account_reference="BOOK123", transaction_desc="E-Book Purchase"):
    access_token = get_access_token()
    password, timestamp = generate_password()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": MPESA_CALLBACK_URL,
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc
    }

    response = requests.post(f"{MPESA_BASE_URL}/mpesa/stkpush/v1/processrequest", json=payload, headers=headers)
    return response.json()
