import requests

API_KEY = "537b09cd56c297c0712f4aee4197f6e8"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "lat": 41.878113,
    "lon": 87.629799,
    "appid": API_KEY
}

r = requests.get(OWM_ENDPOINT, params=weather_params)
print(r.status_code)


