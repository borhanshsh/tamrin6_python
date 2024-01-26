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
    item1=str(item)
    item2=item1.replace('\\','$')
    for i in range(len(item2)):
        if item2[i]=='$' and item2[i+1]=='n':
            print()
        elif item2[i]=='n' and item2[i-1]=='$':
            pass
        else:
            if item2[i]=='$':
                print('\\',end='')
            else:
                print(item2[i],end='')
    print('',end=' ')        
            
