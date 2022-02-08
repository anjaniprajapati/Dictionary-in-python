list1=[{"first":"1"},
{"second": "2"}, 
{"third": "1"}, 
{"four": "5"}, 
{"five":"5"}, 
{"six":"9"},
{"seven":"7"}
]
l=[]
l1=[]
for i in list1:
    for j in i.values():
        l.append(j)
        k=0
        while k<len(l):
            if l[k] not in l1:
                l1.append(l[k])
            k+=1
print(l1)

