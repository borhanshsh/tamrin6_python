#this code get cleaned
name_tale=input()
if name_tale=='sum':
    sum=0
    while True:
        adad=input()
        if adad=='end':
            print(sum)
            break
        adad=int(adad)
        sum+=adad
elif name_tale=='average':
    sum=0
    shomarande=0
    while True:
        adad=input()
        if adad=='end':
            average=sum/shomarande
            if ((average*1000)%10)==5:
                average=average+0.01
            if (average*100)%10<1:
                print("%.1f"%average)
            else:
                print("%.2f"%average)
            break
        shomarande+=1
        sum+=int(adad)        
elif name_tale=='lcd':
    icd=int(input())
    while True:
        adad=input()
        if adad=='end':
            print(icd)
            break
        adad=int(adad)
        a=0
        b=0
        if adad>icd:
            a=adad
            b=icd
        else:
            a=icd
            b=adad
        while True:
            if a%b==0:
                icd=int(icd*(adad/b))
                break
            else:
                c=a
                a=b
                b=c%b
elif name_tale=='gcd':
    gcd=int(input())
    while True:
        adad=input()
        if adad=='end':
            print(gcd)
            break
        adad=int(adad)
        a=0
        b=0
        if adad>gcd:
            a=adad
            b=gcd
        else:
            a=gcd
            b=adad
        while True:
            if a%b==0:
                gcd=b
                break
            else:
                c=a
                a=b
                b=c%b
elif name_tale=='min':
    adad_0=input()
    min=int(adad_0)
    while True:
        adad=input()
        if adad=='end':
            print(min)
            break
        if int(adad)<min:
            min=int(adad)
elif name_tale=='max':
    adad_0=input()
    max=int(adad_0)
    while True:
        adad=input()
        if adad=='end':
            print(max)
            break
        if int(adad)>max:
            max=int(adad)
else:
    print('Invalid command')    
    