dic={'1':['a','b'], '2':['c','d']}
l=[]
l1=[]
for i in dic:
    for j in dic[i]:
        l.append(j)
        for k in l:
            l1.append(k)
print(l1