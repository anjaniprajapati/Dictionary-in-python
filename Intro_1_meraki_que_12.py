from re import I


n=int(input("enter any no::"))
d={}
i=1
while i<=n:
    exs=i*i 
    d.update({i:exs})
    i+=1
print(d)
