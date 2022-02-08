def anj(dict,n):
    re=all(x==n for x in dict.values())
    return re
students = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}

n=12
print(anj(students,n)) 

n=10
print(anj(students,n))




