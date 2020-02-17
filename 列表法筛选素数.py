maxnumber=int(input("please input a number more than 2:\n"))
lst=list (range(2,maxnumber))
m=pow(maxnumber,0.5)
for index,values in enumerate(lst):
    if values>m:
        break
    lst[index+1:]=filter(lambda x:x%values!=0,lst[index+1:])
print(lst)
