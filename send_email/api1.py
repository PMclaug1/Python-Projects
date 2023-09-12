import requests
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude,latitude)
print(iss_position)

parameters = {
    "lat": latitude,
    "long": longitude,
    "formatted": 0
}

sunrise_response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

sunrise_data = sunrise_response.json()
sunrise = sunrise_data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = sunrise_data["results"]["sunset"].split("T")[1].split(":")[0]
weather_data = (sunrise, sunset)

print(weather_data)

time_now = datetime.now()

print(time_now.hour)