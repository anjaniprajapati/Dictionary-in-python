# n1=int(input("enter any number::"))
# n2=int(input("enter an nuber2:"))
# m={}
# while n1<=n2:
#     n=[]
#     j=1
#     while j<=10:
#         e=n1*j
#         n.append(e)
#         j+=1
#     m[n1]=n
#     n1+=1
# print(m)

a=[[2,3,4],[5,6,[7]]]
i=0
s=0
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    s=s+a[i][j][k]
                    k+=1
            else:
                s=s+a[i][j]
            j+=1
    else:
        s=s+a[i]
    i+=1
print(s)
