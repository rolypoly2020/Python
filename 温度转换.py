#temconvert.py
x=input("please input a tempture with C/F:\n")
if x[-1] in ['C','c']:
    c=eval(x[:-1])
    f=c*1.8+32
    ''' print("转换后的华氏温度%.2f F"%f)'''
    print("转换后的华氏温度{:.2f}F".format(f))
elif x[-1] in ['F','f']:
    f=eval(x[:-1])
    c=(f-32)/1.8
    ''' print("转换后的摄氏温度%.2f C"%c)'''
    print("转换后的摄氏温度{:.2f}C".format(c))
else:
    print("it is wrong input")
