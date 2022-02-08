n=int(input("enter len ::"))
d={}
for i in range(1,n+1):
    n1=input("enter key::")
    v=int(input("enter values::"))
    d.update({n1:v})
print(d)
b = sorted(d.keys())
print("Sorted keys",b)
c = sorted(d.items())
print("Sorted Values",c) 






# dict = {6:'George' ,2:'John' ,1:'Potter' ,9:'Micheal' ,7:'Robert' ,8:'Gayle' }  
 
# b = sorted(dict.keys())
# print("Sorted keys",b)  
  
# c = sorted(dict.items())
# print("Sorted Values",c)