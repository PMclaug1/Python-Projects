import requests
from datetime import datetime

API_KEY = "d1b07860e7112be40bc7ac7ec671dbba"
APP_ID = "383a80b4"

GENDER = "MALE"
HEIGHT_CM = 183
WEIGHT_KG = 91
AGE = 34

exercise_stats_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/92ec6617ca4c1884063725bfb45d1321/myWorkouts/workouts"

exercise_prompt = input("Tell me what exercises you did today. ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": exercise_prompt,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_stats_endpoint, json=exercise_params ,headers=headers)
result = response.json()
print(result)

todays_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

GOOGLE_SHEET_NAME = "workout"

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": todays_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    username = "pmclaug1"
    password = "p-241121"

    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        auth=(
            username,
            password
        )
    )

    print(f"Sheety Response: \n {sheet_response.text}")

sheety_header = {
    "Authorization": "Basic cG1jbGF1ZzE6cC0yNDExMjE=",
    "username": "pmclaug1",
    "password": "p-241121"
}

