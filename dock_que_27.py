student = [{'id': 1, 'success': False, 'name': 'Lary'},
 {'id': 2, 'success': True, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

c=0
for i in student:
    for j in i.values():
        if j!=True:
            c+=1
            print(c)