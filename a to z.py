num=int(input("enter number"))
m=[]
# c=0
for i in range(num):
    p=chr(65+i)
    m.append(p)
    # c+=1
i=0
n={}
c=0
while i<len(m):
    l=m[i]
    n[l]=i
    i=i+1
    c+=1
print(n)
print('total no=',c)
