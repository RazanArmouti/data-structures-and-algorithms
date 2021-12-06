def mergeSort(alist):
    print("Splitting",alist)
    n=len(alist)
    if n>1:
        mid=n//2
        lefthalf=alist[:mid]
        righthalf=alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        merge(lefthalf,righthalf,alist)
    return alist

def merge(lefthalf,righthalf,alist):
    i=0
    j=0
    k=0
    while i<len(lefthalf) and j<len(righthalf):
        if lefthalf[i]<=righthalf[j]:
            alist[k]=lefthalf[i]
            i=i+1
        else:
            alist[k]=righthalf[j]
            j=j+1
        k=k+1
    if i<len(lefthalf):
        alist[k]=lefthalf[i]
        i=i+1
        k=k+1
    elif j<len(righthalf):
        alist[k]=righthalf[j]
        j=j+1
        k=k+1
    print("merging",alist)

if __name__=="__main__":
    alist=[8,4,23,42,16,15]
    mergeSort(alist)
    print(alist)
