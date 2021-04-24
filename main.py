from datetime import datetime
from threading import Timer
import os

x=datetime.today()
y=x.replace(day=x.day+1, hour=1, minute=0, second=0, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

ip = input("IP Adress: ")
username = input("Username: ")
password = input("Password: ")

def shutdown():
    os.system("net rpc -S -U" + ip + username+"%"+password ("shutdown -t 1 -f"))
    
print("If all fields were correct the computer will shutdown automaticly in 1 day and 1 hour")
t = Timer(secs, shutdown)
t.start()