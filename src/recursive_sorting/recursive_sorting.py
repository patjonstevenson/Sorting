# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    # merged_arr = [0] * elements
    merged_arr = []
    # TO-DO
    # Keep looping while one of the arrays has elements
    while len(arrA) or len(arrB):
        # Check for arrA to be empty
        if not len(arrA):
            # If arrA empty, add all of arrB to the new_array.
            # This will also have the effect of ending whte while loop.
            merged_arr.extend(arrB)
            arrB = []

        # Check for arrB to be empty
        elif not len(arrB):
            # If arrB empty, add all of arrA to the new_array.
            # This will also have the effect of ending whte while loop.
            merged_arr.extend(arrA)
            arrA = []

        # If the first element of A is bigger than the first element of B,
        # pop it off and add it to the new array.
        elif arrA[0] < arrB[0]:
            el = arrA.pop(0)
            merged_arr.append(el)

        # If the first elements of each array are equal, add them both
        # to the new array, going from left to right.
        # Commented out because I think this might result in an unstable sort.
        # elif arrA[0] == arrB[0]:
        #     el1 = arrA.pop(0)
        #     merged_arr.append(el1)
        #     el2 = arrB.pop(0)
        #     merged_arr.append(el2)

        # If the first element of B is bigger than the first element of A,
        # pop it off and add it to the new array.
        else:
            el = arrB.pop(0)
            merged_arr.append(el)

    # Once the while loop has terminated, return the new array. 
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
