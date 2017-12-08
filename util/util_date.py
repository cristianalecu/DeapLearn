import datetime
from numpy.f2py.crackfortran import beginpattern

def date_passed_seconds():
    now = datetime.datetime.now()
    beg_year = datetime.datetime(now.year,1,1,0,0,0,0)
    delta = now - beg_year
    print(delta.total_seconds())

def date_format():
    now = datetime.datetime.now()
    print(str(now))
    print(now.strftime("%Y-%m-%d-%H-%M-%S-%f"))

date_passed_seconds()
date_format()