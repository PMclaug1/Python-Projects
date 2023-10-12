import requests
import time


API_KEY = "537b09cd56c297c0712f4aee4197f6e8"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": 41.878113,
    "lon": -87.629799,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "units": "imperial"
}


r = requests.get(OWM_ENDPOINT, params=weather_params)
r.raise_for_status()
weather_data = r.json()
condition_code = weather_data["weather"][0]["id"]
if int(condition_code) < 700:
    print("Bring an umbrella.")
else:
    print("All clear.")

# if weather ID is < 700 print that you need an umbrella

