d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
dict={}
for i in d1:
    for j in d2:
        if i==j:
            dict[j]=d1[i]+d2[j]
else:
    dict[i]=d1[i]
    dict[j]=d2[j]
print(dict)