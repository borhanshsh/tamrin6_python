list=input().split()
list2=[]
for item in list:
    list2.append('.')
for item in list:
    item_asli=''
    character=item[0]
    for j in range(len(item)):
        if j!=0:
            item_asli+=item[j]
    list2[int(item_asli)]=character
for item in list2:
    print(item,end='')