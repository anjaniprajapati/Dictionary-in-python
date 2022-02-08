n=int(input("enter len ::"))
d={}
for i in range(1,n+1):
    n1=input("enter key::")
    v=int(input("enter values::"))
    d.update({n1:v})
print(d)
d.popitem()
print(d)