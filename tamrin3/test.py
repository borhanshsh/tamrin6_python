list1=input().split()
list2=[]
tedad_a=0
for item in list1:
    d=''
    for i in range(len(item)):
        if item[i]=="@":
            tedad_a+=1
        if item[i]=="#" and tedad_a>0:
            tedad_a-=1
        else:
            d=d+item[i]
    list2.append(d)
print("Formatted Text: ",end='')
for item in list2:
    for i in range(len(item)):
        if (item[i-1]+item[i])=='\n':
            print()
        else:
            print(item[i],end='')
    print('',end=' ')