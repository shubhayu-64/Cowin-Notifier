import requests
from datetime import date
from datetime import datetime
import json
from pprint import pprint


def update_DateTime():
    today = date.today()
    day = today.strftime("%d-%m-%y")
    print(day)
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    print(time)

    with open("data.json", "r") as data:
        preData = json.load(data)
    preData["date"] = day
    preData["time"] = time
    with open("data.json", "w") as data:
        json.dump(preData, data)


if __name__ == "__main__":
    with open("districts.json", "r") as file:
        fetch = json.load(file)
    today = date.today()
    day = today.strftime("%d-%m-%y")
    districts = fetch['districts']
    for element in districts:
        district_id = element['district_id']
        link = f"https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={district_id}&date={day}"
        response = requests.get(link)
        data = response.json()
        for centers in data['centers']:
            block_name = centers['block_name']
            district_name = centers['district_name']
            name = centers['name']
            pincode = centers['pincode']
            fee = centers['fee_type']
            for sessions in centers['sessions']:
                date = sessions['date']
                min_age_limit = sessions['min_age_limit']
                msg = f"Vaccine appointment available for: \n\n - Age: {min_age_limit}+ \n - On: {date}\n - Fee: {fee} \n\nIn {name}, {block_name}, {district_name}, {pincode} \n#COVID19 #COVID19Vaccine #CovidIndia #vaccination"
                print(msg)

    '''
    response = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=725&date=03-05-2021")
    data = response.json()
    for centers in data['centers']:
        block_name = centers['block_name']
        district_name = centers['district_name']
        name = centers['name']
        pincode = centers['pincode']
        fee = centers['fee_type']
        for sessions in centers['sessions']:
            date = sessions['date']
            min_age_limit = sessions['min_age_limit']
            msg = f"Vaccine appointment available for: \n\n - Age: {min_age_limit}+ \n - On: {date}\n - Fee: {fee} \n\nIn {name}, {block_name}, {district_name}, {pincode} \n#COVID19 #COVID19Vaccine #CovidIndia #vaccination"
            print(msg)'''
