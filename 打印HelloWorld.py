x=int(input("请输入一个整数"))
str='Hello World'
if x==0:
    print(str)
elif x>0:
    print(str[:2])
    print(str[2:4])
    print(str[4:6])
    print(str[6:8])
    print(str[8:10])
else:
    for i in str:
        print(i)