import smtplib
import datetime as dt

my_email = "test_email@gmail.com"
password = "iqws wmbl nceg fwwy"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="email_to_goes_here", msg="Subject:Test Email\n\nBody of email")
    connection.close()

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if year == 2023:
    print("Test")

date_of_birth = dt.datetime(year=1990, month=10, day=1)



