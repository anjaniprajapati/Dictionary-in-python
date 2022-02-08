# d1= {'key1': 1, 'key2': 3, 'key3': 2}
# d2= {'key1': 1, 'key2': 2}
# for i,j in d1.items():
#     if i in d2 and d1[i]==d2[i]:
#         print({i:j})



       



# dict=input("enter any name::")

# dict1={}    
# i=0
# while i<len(dict):
#     dict1[dict[i]]=dict
#     i+=1
# print(dict1)

     
# l1=["a","b"]
# l2=[1,2]
# l=[]
# l3=[]
# l4=[]
# l5=[]
# for i in l1:
#     for j in l2:
#         a=l1[0],l2[0]
#         b=l1[1],l2[0]
#         c=l1[0],l2[1]
#         d=l1[1],l2[1]
# l.append(a)
# l3.append(b)
# l4.append(c)
# l5.append(d)
# s=l+l3
# s1=l4+l5
# print([s,s1])


# n=input("enter::")
# i=0
# dict={}
# while i<len(n):
#     dict[n[i]]=i
#     i+=1
# print(dict)




# dict=input("enter any name::")

# dict1={}
# i=0
# while i<len(dict):
#     ch=(dict[i])
#     if ch not in dict1:
#         dict1[ch]=[]
#     dict1[ch].append(dict)
#     i+=1

# print(dict1)

# dict={"one":[1,2,3,4],"two":[5,6,7,8],"tree":[9,10,11,12]}
# l1=[]
# l2=[]
# for i in dict:
#     for j in dict[i]:
#         if j%2==0:
#             l1.append(j)
#         else:
#             l2.append(j)
# print("Even no=",l1)
# print("Odd no=",l2)


# dic={"one":[1,2,3,4],"two":[5,6,7,8],"tree":[9,10,11,12]}
# l1=[]
# l2=[]
# d={}
# for i in dic:
#     for j in dic[i]:
#         if j%2==0:
#             l1.append(j)
#         else:
#             l2.append(j)
# d1=dict(zip(l2,l1))
# print(d1)



     
l1=["a","b"]
l2=[1,2]
n=[]
n1=[]
i=0
while i<len(l2):
    j=0
    while j<len(l1):
        a=l1[j],l2[i]
        n.append(a)
        j=j+1
    i=i+1
# n1.append(n)  
print([n])
