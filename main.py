import requests
import time
import json
import hashlib


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


def authInitiate():
    generateOTP = {"mobile": fetchData("mobile")}
    Response = requests.post(
        "https://cdn-api.co-vin.in/api/v2/auth/public/generateOTP", json=generateOTP)
    if Response.status_code == 200:
        data = Response.json()
        updateData('txnId', data['txnId'])
        print("OTP send successfully.\n")
        updateData("success", "True")

    elif Response.status_code == 400:
        print("Can't send OTP right now. Please try again later.")
    else:
        print("Uh oh! I think I'm lost.")


def authConfirm():
    if fetchData("success") == "True":
        pin = input("Enter your OTP: ").encode('utf-8')
        confirmOTP = {"otp": hashlib.sha256(
            pin).hexdigest(), "txnId": fetchData("txnId")}
        Response = requests.post(
            "https://cdn-api.co-vin.in/api/v2/auth/public/confirmOTP", json=confirmOTP)
        if Response.status_code == 200:
            data = Response.json()
            updateData('token', data['token'])
            print("Yay! OTP confirmed successfully.")

        elif Response.status_code == 400:
            updateData("success", "False")
            print("Can't verify OTP right now. Please try again later.")
        else:
            updateData("success", "False")
            print("Uh oh! I think I'm lost.")
    else:
        pass


if __name__ == "__main__":
    authInitiate()
    authConfirm()
