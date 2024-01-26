checknumber=int(input())
test=False
shomarande=0
for j in range(checknumber-2):
    if (checknumber%(j+2))==0:
        test=True
        print('yes')
        break
if test==False:
    shomarande+=1
print(shomarande)            