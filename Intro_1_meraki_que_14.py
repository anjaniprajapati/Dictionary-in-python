dict={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
for i in dict:
    for j in dict:
        if dict[i]<dict[j]:
            r=dict[i]
            dict[i]=dict[j]
            dict[j]=r
            
print(dict)