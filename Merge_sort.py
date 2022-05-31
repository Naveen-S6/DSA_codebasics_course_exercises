def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_array(left, right, arr)


def merge_two_sorted_array(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


if __name__ == "__main__":
    ar = [[2,5,64,1,26,4,75,33,65,22,6,23,76,32,200],
           [1,2,34,5],
           [],
           [90,88,45,32,21,1],
           [30,20,302,3]]
    #arr = merge_two_sorted_array(arr1, arr2)

    for arr in ar:
        merge_sort(arr)
        print(arr)



