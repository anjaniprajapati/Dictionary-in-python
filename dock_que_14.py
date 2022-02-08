# multiplay of values

n=int(input("enter len of dictionary::"))
dic={}
for i in range(1,n+1):
    n=input("enter key::")
    v=int(input("enter value::"))
    dic.update({n:v})
    s=1
    for x in dic.values():
        s*=x
print( dic)
print(s)

# multiplay of keys

# n=int(input("enter len of dictionary::"))
# dic={}
# for i in range(1,n+1):
#     n=input("enter key::")
#     v=int(input("enter value::"))
#     dic.update({v:n})
#     s=1
#     for x in dic.keys():
#         s*=x
# print( dic)
# print(s)