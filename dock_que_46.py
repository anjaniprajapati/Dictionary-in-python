# d=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# result = [dict([a, int(x)] for a, x in b.items()) for b in d]
# print(result)


d=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
result = [dict([a ,int(x)] for a,x in b.items()) for b in d]
result1= [dict([a ,float(x)] for a,x in b.items()) for b in d]
print(result)
print(result1)