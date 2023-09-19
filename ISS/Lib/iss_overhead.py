import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 41.878113
MY_LONG = -87.629799
MY_EMAIL = "testemail@gmail.com"
MY_PASSWORD = "testpassword"


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

while True:
    #run every 60s
    time.sleep(60)
    if iss_overhead() and is_night():
        connection = smtplib.SMTP(smtp.gmail.com)
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: ISS Update\n\nThe ISS is overhead."
        )
