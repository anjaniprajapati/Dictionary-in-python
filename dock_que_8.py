n=int(input("enter len::"))
dict={}
for i in range(1,n+1):
    name=input("enter name::")
    value=int(input("enter value::"))
    dict.update({name:value})
    if name in dict:
        print(name,"yes")
    elif value in dict:
        print(value,"hii")
    else:
        print("not here present")
