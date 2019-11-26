import time
from datetime import datetime as dt

hosts = "C:/Windows/System32/drivers/etc/hosts"
redirect = '127.0.0.1'
website_list = ['www.facebook.com', "www.netflix.com"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,20):
        print("RIhanna")
        file = open(hosts, 'r+')
        content = file.read()
        for website in website_list:
            if website in  content:
                pass
            else:
                file.write('#           ' + redirect+ ' '+website + '\n')
    else:
        print("Drake")

        file = open(hosts,'r+')
        content = file.readlines()
        file.seek(0)

        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
            file.truncate()

    time.sleep(5)

