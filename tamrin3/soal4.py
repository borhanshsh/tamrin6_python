list1=map(int,input().split())
b=int(input())
dict1={}
test=False
list_ans=[]
for idx, item in enumerate(list1):
    dict1[item]=idx
for x in dict1:
    z=b-x
    if z in dict1:
        if z>x:
            list_ans.append(dict1[z]+dict1[x])
list_ans.sort()
if list_ans==[]:
    print('Not Found!')
else:
    for item in list_ans:
        print(item)
    
