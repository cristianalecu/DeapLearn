import datetime

def time_delta(t1, t2):
    delta = t2 - t1
    return delta

def date_passed_seconds():
    now = datetime.datetime.now()
    beg_year = datetime.datetime(now.year,1,1,0,0,0,0)
    delta = now - beg_year
    return delta.total_seconds()

def date_format():
    now = datetime.datetime.now()
    #print(str(now))
    return now.strftime("%Y-%m-%d-%H-%M-%S-%f")

t1=datetime.datetime(2017,10,29,0,0,0)
t2=datetime.datetime(2017,10,30,0,0,0)
t3=t1 + datetime.timedelta(days=1)
d = time_delta(t1, t2)
d2 = time_delta(t1, t2)

print(d ,  d.total_seconds(), t2)
print(d2 ,  d2.total_seconds(), t3)

print (date_passed_seconds())
print (date_format() )