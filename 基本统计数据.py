def getnum():
    nums=[]
    n=input("请输入一个数字，按回车退出:")
    while n!="":
        nums.append(eval(n))
        n=input("请输入一个数字，按回车退出:")
    return nums
def mean(nums):
    s=0
    for i in nums:
         s=s+i    
    a=s/len(nums)
    return a
def fanc(nums,mean):
    d=0.0
    for n in nums:
        d=d+(n-mean)**2
    return pow(d/(len(nums)-1),0.5)
def mudium(nums):
    sorted(nums)
    if len(nums)%2==0:
        m= nums[len(nums)//2]
    else:
        m= (nums[len(nums)//2-1]+nums[len(nums)//2])/2
    return m
n=getnum()
m=mean(n)
print("平均数:{},方差:{},中位数:{}".format(m,fanc(n,m),mudium(n)))
        

    


