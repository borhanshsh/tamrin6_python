#this code get cleaned
number1=int(input())
number2=int(input())
test=int(input())
while True:
    if (number1 & number2)==0:
        break
    number3=number1
    number4=number2
    number1=((number3 & number4) << 1)
    number2=number3 ^number4
ans=(number1  | number2)      
print(ans)
if test==ans:
    print('YES')
else:
    print('NO')
    
        
        