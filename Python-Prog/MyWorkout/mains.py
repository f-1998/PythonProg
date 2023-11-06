import requests
from datetime import datetime


APP_KEY =  "123ujhgvutyy765" #Your APP_key of  Nutritionix
APP_ID = "123ujhgvutyy765" #Your APP_ID of  Nutritionix

USER_ID = "xyz123" 

nutrition_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell which exercise you did today?: ")
sheety_endpoint = "https://api.sheety.co/0ff149dcfdaac89aaf18f5a807fb327e/myWorkout/sheet1"


GENDER = "FEMALE"
WEIGHT_KG = 50
HEIGHT = 150
AGE = 25

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "x-remote-user-id": "0"

}
x = datetime.now()
date = x.strftime(f"%d/%m/%y")
time = x.strftime(f"%H:%M:%S")



response = requests.post(url=nutrition_endpoint, json=parameters, headers=header)
response.raise_for_status()
result = response.json()


for i in result['exercises']:
    sheet_inputs = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }
    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        auth=(
            "xyz", #your sheety username
            "password", #your sheety password
        )
    )
