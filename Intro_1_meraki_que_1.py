dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
c={}
for i in dic1:
    for j in dic2:
        for k in dic3:
            if i==j:
                c[j]=dic1[i]+dic2[j]
            else:
                c.update(dic1)
                c.update(dic2)
                c.update(dic3)

print(c)

# dic1={1:10,2:20}
# dic2={3:30,2:10}
# dic3={7:50,5:60}
# m={}
# for i in dic1:
# 	for j in dic2:
# 		for k in dic3:
# 			if i==j:
# 				m[j]=dic1[i]+dic2[j]
# 			else:
# 				m.update(dic1)
# 				m.update(dic2)
# 				m.update(dic3)
# print(m)