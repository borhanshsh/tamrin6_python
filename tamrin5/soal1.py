import re
def mergeSort(array):
    if len(array) >1:
        mid=len(array)//2
        L=array[:mid]
        R=array[mid:]
        mergeSort(L)
        mergeSort(R)
        l=0
        r=0 
        k=0
        while l<len(L) and r<len(R):
            if L[l]<R[r]:
                array[k]=L[l]
                l+=1
            else:
                array[k]=R[r]
                r+=1
            k+=1
        while l<len(L):
            array[k]=L[l]
            l+=1
            k+=1
        while r<len(R):
            array[k]=R[r]
            r+=1
            k+=1
        return (''.join(array))
class Lobster:
    def __init__(self,dna):
        self.dna=dna
        self.dna+=self.dna[0:10]
    def Get_dna(self):
        dna2=''
        test=0
        for i in range(len(self.dna)-1):
            if test==0:
                if self.dna[i]=='t'and self.dna[i+1]=='t':
                    dna2+='o'
                    test=1
                else:
                    dna2+=self.dna[i]
            else:
                test=0
        if test==0:
            dna2+=self.dna[-1]
        return dna2
    def answer(self):
        return self.dna
class Bob(Lobster):
  def __init__(self,dna):
        super().__init__(dna)
class Oktapous:
    def __init__(self):
        pass
    def Get_DNA(self,dna):
        dna=str(dna)
        toll=len(dna)
        i=0
        while True:
            if 'x' in dna:
                if dna[i]=="x":
                    dna+=str(i)
                    break
                if i==toll:
                    break
            else:
                break
            i+=1
        pattern=re.compile(r'(?:aaa|bbb|ccc|qqq|www|eee|rrr|ttt|yyy|uuu|iii|ooo|ppp|sss|ddd|fff|ggg|hhh|jjj|kkk|lll|zzz|xxx|ccc|vvv|nnn|mmm)')
        dna=re.sub(pattern,'(0_0)',dna)
        return dna
            


a=input()
a1=a[::-1]
if a[0]=='m':
    lobster=Lobster(a)
    print(lobster.Get_dna())
elif a[0]=='s' and a[1]=='b':
    bob=Bob(a)
    print(mergeSort(list(str(len(bob.answer())))))
elif a[0]=='s' and a[1]!='b':
    oktapous=Oktapous()
    print(oktapous.Get_DNA(a))
elif a1[0]=='m':
    lobster=Lobster(a1)
    print(lobster.Get_dna())
elif a1[0]=='s' and a1[1]=='b':
    bob=Bob(a1)
    print(mergeSort(list(str(len(bob.answer())))))
elif a1[0]=='s' and a1[1]!='b':
    oktapous=Oktapous()
    print(oktapous.Get_DNA(a1))
else:
    print("invalid input")
