#daydayupq1.py
dayup=pow(1.001,365)
daydown=pow(0.999,365)
print("{:.2f}, {:.2f}".format(dayup,daydown))
#daydayupq2.py
dayfactor=0.005
dayup=pow(1+dayfactor,365)
daydown=pow(1-dayfactor,365)
print("{:.2f} ,{:.2f}".format(dayup,daydown))
#daydayupq3.py
dayup=1.0
dayfactor=0.01
for i in range(365):
    if i%7 in [6,0]:
        dayup=dayup*(1-dayfactor)
    else:
        dayup=dayup*(1+dayfactor)
print("{:.2f}".format(dayup))
#daydayupq4.py
def day(df):
    dayup=1
    for i in range(365):
        if i%7 in [6,0]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfactor=0.01
while day(dayfactor)<37.78:
    dayfactor+=0.001
print("{:.3f}".format(dayfactor))


