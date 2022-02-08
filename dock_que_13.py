

n=int(input("enter len of dictionary::"))
dic={}
for i in range(1,n+1):
    n=input("enter key::")
    v=int(input("enter value::"))
    dic.update({n:v})
    print( dic)
    s=0
    for x in dic.values():
        s+=x
print(s)


