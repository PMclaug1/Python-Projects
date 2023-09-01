import datetime as dt
import pandas
import random

today = (dt.datetime.now().month, dt.datetime.now().day)
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"