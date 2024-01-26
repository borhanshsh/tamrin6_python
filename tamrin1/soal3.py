#this code get cleaned
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
reversebineradadkoli=''
while True:
    if adadkoli%2==1:
        adadkoli-=1
        reversebineradadkoli=reversebineradadkoli+'1'
    else:
        reversebineradadkoli=reversebineradadkoli+'0'
    adadkoli=adadkoli/2
    if adadkoli<1:
        break
bineradadkoli=''
for i in range(len(reversebineradadkoli)):
    bineradadkoli=bineradadkoli+reversebineradadkoli[-i-1]
vorodi=[]
for i in range(n):
    a=int(input())
    vorodi.append(a)
for item in vorodi:
    if bineradadkoli[(item-1)]=='0':
        print('no')
    else:
        print('yes')