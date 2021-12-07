def quick_sort(list, left, right):
    print(list)
    if left<right:
        position = partition(list,left,right)
        print(position)
        quick_sort(list,left,position-1)
        quick_sort(list,position+1,right)
    return list

def partition(list, left, right):
    pivot=list[right]
    print("pivot",pivot)
    low= left -1
    print("flow",low)

    for i in range(left,right):
        if list[i]<=pivot:
            low +=1
            swap(list,i,low)
    swap(list,right,low+1)
    print("low",low)
    return low +1

def swap(list,i,low):
    temp=list[i]
    list[i]=list[low]
    list[low]=temp


if __name__=="__main__":
    arr=[8,4,23,42,16,15]
    n=len(arr)
    print(quick_sort(arr,0,n-1))

