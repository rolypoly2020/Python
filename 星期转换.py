#weekprint1.py
weekstr="星期一星期二星期三星期四星期五星期六星期日"
weeknum=eval(input("请输入1-7的数字:"))
if(weeknum>7 or weeknum<1):
    print("please input another one ")
x=3*(weeknum-1)
print(weekstr[x:x+3])
#方法二
weekstr='一二三四五六七'
weeknum=eval(input("请输入1-7的数字"))
print("星期"+weekstr[weeknum-1])