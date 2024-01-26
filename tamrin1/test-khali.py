tike1=int(input())
tike2=int(input())
n=int(input())
"""
i=0
tike3=tike1
while True:
   if tike3>1:
       i+=1
   else:
       break
   tike3=tike3//10
"""
adadkoli=tike2*(10**(32))+tike1
bineradadkoli=''
while True:
    if adadkoli%2==1:
        adadkoli-=1
        bineradadkoli='1'+bineradadkoli
    else:
        bineradadkoli='0'+bineradadkoli
    adadkoli=adadkoli/2
    if adadkoli<1:
        break
print(bineradadkoli)