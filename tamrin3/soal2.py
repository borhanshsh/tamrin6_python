n=int(input())
list1=[]
for i in range(n):
    test=False
    b=input()
    d=''
    for j in range(len(b)):
        if test==True:
            d=d+b[j]
        if b[j]=='@':
            test=True
    list1.append(d)
set1={list1[0]}
for item in list1:
    set1.add(item)
list2=(list(set1))
list2.sort()
for item in list2:
    print(item)