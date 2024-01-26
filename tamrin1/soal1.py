number1=int(input())
number2=int(input())
i=0
j=0
binernumber1=''
binernumber2=''
while True:
    if number1//(2**i)>1:
        i+=1
    else:
        break
while True:
    if number1//(2**i)==1:
        binernumber1=binernumber1+'1'
        number1=number1-2**i
    else:
         binernumber1=binernumber1+'0'

    if i==0:
        break
    i-=1
while True:
    if number2//(2**j)>1:
        j+=1
    else:
        break
while True:
    if number2//(2**j)==1:
        binernumber2=binernumber2+'1'
        number2=number2-2**j
    else:
         binernumber2=binernumber2+'0'

    if j==0:
        break
    j-=1
toolbiner1=len(binernumber1)
toolbiner2=len(binernumber2)
toolkamtar=toolbiner1
if toolbiner2<toolbiner1:
    toolkamtar=toolbiner2
tooldifferent=toolbiner1+toolbiner2-2*toolkamtar
different=0
for i in range(toolkamtar):
    if binernumber1[-i-1]!=binernumber2[-i-1]:
        different+=1
different=different+tooldifferent
print(different)

    
        
    