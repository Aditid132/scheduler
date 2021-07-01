# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 19:33:01 2021

@author: aditi
"""

import schedule  
  
def job():  
    print("A Simple Python Scheduler.")  
  
# run the function job() every 2 seconds  
schedule.every(2).seconds.do(job)  
  
while True:  
    schedule.run_pending()
    
import schedule
import time

def job():
    print("I'm working...")

def job2():
    print("yo boiss..")

def job3():
    print("Hello")
    
schedule.every(5).seconds.do(job)
# some other variations 
schedule.every().hour.do(job)
schedule.every().day.at("12:25").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().thursday.at("19:15").do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)
schedule.every(2).seconds.do(job2)

while True:
    schedule.run_pending()
    time.sleep(1)
    
import smtplib
  
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("youremail", "yourpassword")
  
msg = "FIRST EMAIL USING PYTHON!"
server.sendmail("youremail", "email-of-receiver", msg)
server.quit()
print("Email Sent")