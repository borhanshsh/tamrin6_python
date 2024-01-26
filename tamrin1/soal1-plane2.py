number1=int(input())
number2=int(input())
number3= number1^number2
shomarande=0
while True:
    if number3%2!=0:
        number3=number3-1 
        shomarande+=1
    number3=number3/2
    if number3==0:
        break
print(shomarande)