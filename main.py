import requests
import time
import json

mobileNumber = {
    "mobile": "7679325872"
}

txnId = {}

if __name__ == "__main__":
    mobResponse = requests.post(
        "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP", json=mobileNumber)
    print(mobResponse)
    txnId = mobResponse.json()
    print(txnId)
