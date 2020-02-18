maxnumber=int(input("please input a number more than 2:\n"))
lst=list (range(2,maxnumber))
m=pow(maxnumber,0.5)
for index,values in enumerate(lst):
    if values>m:
        break
    '''for value1 in lst[:index:-1]:
       
        if value1%values==0:
            lst.remove(value1)'''
    lst[index+1:]=filter(lambda x:x%values!=0,lst[index+1:])
print(lst)
