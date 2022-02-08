
m=int(input("enter any len::"))
i=1
d={}
while i<=m:
    a=input("ennter any name::")
    b=int(input("enter any marks::"))
    d.update({a:b})
    i+=1
print(d)