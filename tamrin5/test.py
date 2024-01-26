dna='mtmtmttk'
dna2=''
test=0
for i in range(len(dna)-1):
    if test==0:
        if dna[i]=='t'and dna[i+1]=='t':
            dna2+='o'
            test=1
    
        else:
            dna2+=dna[i]
    else:
        test=0
if test==0:
    dna2+=dna[-1]
print(dna2)
                