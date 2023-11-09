import requests
from datetime import datetime

API_KEY = "d1b07860e7112be40bc7ac7ec671dbba"
APP_ID = "383a80b4"

exercise_stats_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": "ran 2.5 miles"
}

response = requests.post(url=exercise_stats_endpoint, json=exercise_params ,headers=headers)
print(response.text)