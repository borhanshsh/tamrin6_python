a=int(input())
if a>=1:
    print(1)
list='11'
if a>=2:
    print('1'+' '+'1')
for i in range(a-2):
    list2=[1]
    for j in range(i+1):
        list2.append(int(list[j])+int(list[j+1]))
    list2.append(1)
    list=list2
    for k in range(i+3):
        if k<i+2:
            print(list[k],end=" ")
        else:
            print(list[k])