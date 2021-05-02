import requests
import time
import json

mobileNumber = {
    "mobile": "7679325872"
}


def updateData(key, value):
    with open("data.json", "r") as data:
        preData = json.load(data)
    preData[key] = value
    with open("data.json", "w") as data:
        json.dump(preData, data)


def fetchData(key):
    with open("data.json", "r") as data:
        preData = json.load(data)
    return preData[key]


def authentication():
    mobResponse = requests.post(
        "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP", json=mobileNumber)
    if mobResponse.status_code == 200:
        print(mobResponse)
        res = mobResponse.json()
        print(res['txnId'])
        updateData('txnId', res['txnId'])
    elif mobResponse.status_code == 400:
        print("Can't send OTP right now. Please try again later.")
    else:
        print("Uh oh! I think I'm lost.")


if __name__ == "__main__":
    print(fetchData("mobile"))
    authentication()
