import jieba
txt=open("threekingdoms.txt","r",encoding="utf-8").read()
words=jieba.lcut(txt)
d={}
for i in words:
    if i==1:
        continue
    else:

        d[i]=d.get(i,0)+1
items=list(d.items())
items.sort(ket=lambda x:x[1],reverse=True)
for j in range(15):
    i,item=items[j]
    print("{0:<10}{1:>5}".format(i,item))