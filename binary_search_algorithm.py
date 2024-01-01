def bsa(arr, key):
    mid = len(arr)//2
    low = 0
    high = len(arr)-1
    while (low<=high):
        mid = (high + low)//2
        if arr[mid] < key:
            low = mid+1
        elif arr[mid] > key:
            high = mid -1
        else:
            return (mid, arr[mid])
            
        
print(bsa([1,4,13,15,16,23,44,56,78,79,99], 56))