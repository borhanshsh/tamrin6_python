#this code get cleaned
tike1=int(input())
tike2=int(input())
n=int(input())
binertike1=''
while True:
    if tike1%2==1:
        tike1-=1
        binertike1='1'+binertike1
    else:
        binertike1='0'+binertike1
    if tike1<1:
        break
    tike1=tike1/2
binertike2=''
while True:
    if tike2%2==1:
        tike2-=1
        binertike2='1'+binertike2
    else:
        binertike2='0'+binertike2
    if tike2<1:
        break
    tike2=tike2/2
binerkoli=('0'*(32-len(binertike2)))+binertike2+('0'*(32-len(binertike1)))+binertike1
vorodi=[]
for i in range(n):
    a=int(input())
    vorodi.append(a)
for item in vorodi:
    if binerkoli[-item-1]=='0':
        print('no')
    else:
        print('yes')