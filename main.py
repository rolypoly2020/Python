def getTxt():
    txt=open("hamlet.txt","r").read()
    txt=txt.lower()
    for ch in "\|/.,;:'*&^%$#@!-+=`~?[]{}<>":
        txt=txt.replace(ch," ")
    return txt
hamletTxt=getTxt()
words=hamletTxt.split()
d={}
for word in words:
    d[word]=d.get(word,0)+1
items=list(d.items())
items.sort(key=lambda x:x[-1],reverse=True)
for i in range (10):
    word,d=items[i]
    print("{0:<10}{1:>5}".format(word,d))