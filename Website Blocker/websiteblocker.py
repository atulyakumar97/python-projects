import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
blockedlist=['facebook.com','www.facebook.com','fb.com','m.facebook.com','google.co.in','www.google.co.in','google.com','www.google.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9 , 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17, 30):
        print("Work Hours...")
        f=open(hosts_path,'r+')
        content=f.read()
        print(content)
        for website in blockedlist:
            if website in content:
                continue
            else:
                f.write(redirect+" "+website+'\n')
        f.close()
        time.sleep(5)
    else:
        print("Fun Hours...")
        f=open(hosts_path,'r+')
        contentlist=f.readlines()
        f.seek(0)
        for line in contentlist:
            if not any(website in line for website in blockedlist):
                f.write(line)
        f.truncate()
        for i in contentlist:
            print(i)
        f.close()    
        time.sleep(5)
