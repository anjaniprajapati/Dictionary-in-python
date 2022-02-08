latter=input("enter word::")
dic={}
for x in latter:
    keys=dic.keys()
    if x in keys:
        dic[x]+=1
    else:
        dic[x]=1
print(dic)