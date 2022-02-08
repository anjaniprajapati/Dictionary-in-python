list=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], 
    [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'],
    [5, 'Zachary Simon', 'VII']]
i=0
l2={}
while i<len(list):
    j=0
    str=""
    l=[]
    while j<len(list[i]):
        if list[i].index(list[i][j])==0:
            str=list[i][j]
        else:
            l.append(list[i][j])
        j+=1
    l2[str]=l
    i+=1
print(l2)
