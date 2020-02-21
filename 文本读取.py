fd=open("output.txt",'w+')
ls=["中国","美国","法国"]
fd.writelines(ls)
fd.seek(0)
for line in fd:
    print(line)
fd.close()

