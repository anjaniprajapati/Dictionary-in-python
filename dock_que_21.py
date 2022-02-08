list=[{"V":"S001"}, {"V": "S002"}, 
      {"VI": "S001"}, {"VI": "S005"}, 
      {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
l=[]
l1=[]
for i in list:
    for j in i.values():
        l.append(j)
        k=0
        while k <len(l):
            if l[k] not in l1:
                l1.append(l[k])
            k+=1
print(l1)



