count=0
while count<3:
    name=input()
    password=input()
    if name=='Kate'and password=='666666':
        print("登录成功！")
    else:
        count+=1
        if count==3:
            print('3次输入均有误！退出程序。')