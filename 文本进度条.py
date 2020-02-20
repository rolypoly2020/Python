#wenbenjindutiao.py
import time
print("=========start=========")
for i in range(11):
    a=i*'*'
    b=(10-i)*'.'
    c=i*10
    print('{:^3.0f}%[{}->{}]'.format(c,a,b))
    time.sleep(0.2)
print("=========over=========")