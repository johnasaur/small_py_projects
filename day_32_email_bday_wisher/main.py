from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "some@gmail.com"
MY_PASSWORD = "sometest"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("bithdays.csv")

bday_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}

if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bday_person["name"])

    with smtplib.SMTP() as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=bday_person["email"],
            msg= f"Subject:Happy Birthday!\n\n{contents}"
        )



