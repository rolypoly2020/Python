#wenbenjindutiao.py
import time
scale=50
start=time.perf_counter()
print('start'.center(scale//2,'='))
#print("=========start=========")
for i in range(scale+1):
    a=i*'*'
    b=(scale-i)*'.'
    c=100*(i/scale)
    dur=time.perf_counter()-start
    print('\r{:^3.0f}%[{}->{}]{}'.format(c,a,b,dur),end='')
    time.sleep(0.2)
#print("=========over=========")
print('\n'+'over'.center(scale//2,'='))
#q2.py
import time
for i in range(101):
    print('\r{:3}%'.format(i),end="")
    time.sleep(0.1)