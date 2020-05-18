def climbstairs1(m):
    a=1
    b=2
    c=4
    for i in range(m-3):
        c,b,a=a+b+c,c,b
    return c
    #递推
def climbstairs2(m):
    first3={1:1,2:2,3:4}
    if m in first3.keys():
        return first3[m]
    else:
        return climbstairs2(m-1)+\
                climbstairs2(m-2)+\
                climbstairs2(m-3)
print(climbstairs1(15))
print(climbstairs2(15))

