start='yes'
s=0
while start.lower()=='yes':
    x=input("please input a int ")
    x=eval(x)

    
    if  isinstance(x,int)and 0<=x<=100:
        s=x+s

    else:
        print("error")
    start=input('yes or no\t')
print("sum=",s)