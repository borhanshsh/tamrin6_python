#this code get cleaned

sum=0
test=True
while True:
    bineri_b=''
    sum_magsom=0
    n,b=map(int,input().split())
    if n==-1 & b==-1:
        break
    if b<2 or b>9:
        test=False
    for i in range(1,n+1):
        if n%i==0:
            sum_magsom+=i
    while True:
        if sum_magsom<=0:
            break
        bineri_b=str(sum_magsom%b)+bineri_b
        sum_magsom=sum_magsom//b
    sum+=int(bineri_b)
if test==True:
    print(sum)
else:
    print('invalid base!')