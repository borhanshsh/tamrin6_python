#this code get cleaned

a0,b0=map(int,input().split())
shomarande=0
testmakos=False
if a0>b0:
    b=a0
    a=b0
    testmakos=True
else:
    a=a0
    b=b0
for i in range(b-a+1):
    test=False
    checknumber=a+i
    for j in range(checknumber-2):
        if (checknumber%(j+2))==0:
            test=True
    if checknumber<=1:
        test=True
    if test==False:
        shomarande+=1
if testmakos==False:
    print('main order - amount:',shomarande)
else:
    print('reverse order - amount:',shomarande)            
    
    


