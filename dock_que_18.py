n=int(input("enter len ::"))
d={}
for i in range(1,n+1):
    n1=input("enter key::")
    v=int(input("enter values::"))
    d.update({n1:v})
print(d)
max=0
min=0
for x in d:
    if d[x]>max:
        max=d[x]
    if d[x]<max and d[x]>min:
        min=d[x]
print("Maximum No =",max,"Minimum No =",min)
