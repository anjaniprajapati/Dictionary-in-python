# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print("key  value  count")
# for count, (key, value) in enumerate(dict_num.items(), 1):
#     print(key,'   ',value,'    ', count)




dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print("key","value","count")
count=0
for i in dict_num:
    count+=1
    print(i,"  ",dict_num[i],"   ",count)
