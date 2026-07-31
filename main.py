import smtplib
import random
import datetime as dt
import pandas as pd
import os

email=os.environ.get("MY_EMAIL")
password=os.environ.get("MY_PASSWORD")

current_date=dt.datetime.now()

df=pd.read_csv('birthdays.csv')
date_dic=df.to_dict(orient="records")

for value in date_dic:
    if value['day']==current_date.day and value['month']==current_date.month:
        
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt","r") as file:
            Msg=file.read()
            Msg=Msg.replace("[NAME]",value['name'])
            
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()
            connect.login(user=email,password=password)
            connect.sendmail(from_addr=email,
                            to_addrs=value['email'],
                            msg=f"Subject:Happy\n\n{Msg}"
                            )
