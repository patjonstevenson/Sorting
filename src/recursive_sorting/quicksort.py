def quicksort(arr):
    if len(arr) == 0:
        return arr
    else:
        print(arr)
        pivot = arr[0]
        right = []
        left = []
        for el in arr[1::]:
            if el > pivot:
                right.append(el)
            else:
                left.append(el)
        return quicksort(left) + [pivot] + quicksort(right)

test = [61,40,44,5,2,4,3,1,8,4,9,5,3,2,1,10,11,12,16,4,16,17,20,45,0,2,50,3]

print(quicksort(test))