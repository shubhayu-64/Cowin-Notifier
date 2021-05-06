import requests
from datetime import date
from datetime import datetime
import json
import time
from pprint import pprint
import tweepy
import config


def tweet(msg):
    auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    api = tweepy.API(auth)
    try:
        api.update_status(msg)
    except:
        msg = msg + "⠀"
        api.update_status(msg)


def fetch_data():
    with open("all_districts.json", "r") as file:
        fetch = json.load(file)

    current_date = date.today()
    day = current_date.strftime("%d-%m-20%y")
    districts = fetch['districts']
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    for element in districts:
        district_id = str(element['district_id'])
        if len(district_id) == 1:
            district_id = "00" + district_id
        elif len(district_id) == 2:
            district_id = "0" + district_id
        link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={day}"
        response = requests.get(link, headers=header)
        data = response.json()
        time.sleep(3)
        for center in data['centers']:
            block_name = center['block_name']
            district_name = center['district_name']
            name = center['name']
            pincode = center['pincode']
            fee = center['fee_type']
            state = center['state_name']

            for sessions in center['sessions']:
                cur_date = sessions['date']
                min_age_limit = sessions['min_age_limit']
                if sessions['available_capacity'] > 0 and min_age_limit == 18:
                    # print("Available")
                    msg = f"Vaccine appointment available for: \n\n - Age: {min_age_limit}+ \n - On: {cur_date}\n - Fee: {fee} \n\nIn {name}, {block_name}, {district_name}, {state}, {pincode} \n#COVID19 #COVID19Vaccine #CovidIndia #vaccination #CowinNotifier #WestBengal"
                    print(msg)
                    tweet(msg)
                    time.sleep(30)


if __name__ == "__main__":
    # time.sleep(120)
    print("Bot started!")
    while True:
        fetch_data()
        time.sleep(43200)
