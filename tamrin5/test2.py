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
            array[k]=r[r]
            r+=1
            k+=1
        return (''.join(array))
a=input().split()
print(mergeSort(a))