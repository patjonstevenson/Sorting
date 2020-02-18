# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    is_sorted = False
    while len(arrA) or len(arrB):
        # print(f'arrA: {arrA}')
        # print(f'arrB: {arrB}')
        if not len(arrA):
            # print('arrA empty')
            merged_arr.extend(arrB)
            arrB = []
        elif not len(arrB):
            # print('arrB empty')
            merged_arr.extend(arrA)
            arrA = []
        elif arrA[0] < arrB[0]:
            # print('arrA[0] < arrB[0]')
            el = arrA.pop(0)
            merged_arr.append(el)
        else:
            # print('arrA[0] > arrB[0]')
            el = arrB.pop(0)
            merged_arr.append(el)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # print(f"length of arr: {len(arr)}")
    if len(arr) == 1 or len(arr) == 0:
        # print(f"Returning arr: {arr}")
        return arr
    else:
        # print("Left: {}".format(arr[0:len(arr)//2]))
        # print("Right: {}".format(arr[len(arr)//2::]))
        return merge(merge_sort(arr[0:len(arr)//2]), merge_sort(arr[len(arr)//2::]))

# test = [3,1,4,2]
# sorted_test = merge_sort(test)
# print(sorted_test)

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
