a=int(input())
list=[]
min_khat=1
max_khat=1
location=1
while True:
    harekat=input()
    if harekat=="L" and location>=2:
        location-=1
        if location<min_khat:
            min_khat=location
    elif harekat=='R' and location<a:
        location+=1
        if location>max_khat:
            max_khat=location
    elif harekat=='B':
        for j in range(1,a+1):
            if j>=min_khat and j<=max_khat:
                list.append('*')
            else:
                list.append('.')
        list.append('tamam')
        max_khat=location
        min_khat=location
    elif harekat=='END':
        for j in range(1,a+1):
            if j>=min_khat and j<=max_khat:
                list.append('*')
            else:
                list.append('.')
        list.append('tamam')
        for item in list:
            if item=='*':
                print('*',end=' ')
            elif item=='.':
                print('.',end=' ')
            elif item=='tamam':
                print('')
        if location!=a:
           print("There's no way out!") 
        break
            
               
             