import time as temps
from datetime import datetime
a=''

a=input('enter time in s')
def countdown(t):
    t=int(t)
    time=divmod(t, 60)
    while time[0]+time[1]>0:
        t-=1
        time=divmod(t, 60)
        dt_obj = datetime( 2000,3,3,23,time[0], time[1])
        final_t=dt_obj.strftime("%M:%S")
        print(final_t)
        temps.sleep(1)
    print(t)
    print('Fire in the hole')
    
countdown(a)