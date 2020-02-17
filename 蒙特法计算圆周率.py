from random import random 
times=int(input("请输入投掷飞镖次数:"))
hit=0
for i in range(times):
    x=random()
    y=random()
    if x*x+y*y<=1:
        hit+=1
print("圆周率估计值：",4*hit/times)