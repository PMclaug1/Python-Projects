import requests
import time
from twilio.rest import Client


API_KEY = "537b09cd56c297c0712f4aee4197f6e8"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
account_sid = 'ACe72d733d8d71bfbdf3f874fcb41f563d'
auth_token = '83b9c91a862fe2f626b38c8619cb6335'

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
will_rain = False

if int(condition_code) > 700:
    print("All clear.")
else:
    will_rain = True
    if will_rain:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body="Bring an umbrella.",
            from_="+18884877013",
            to='+16306396125'
        )

        print(message.status)





