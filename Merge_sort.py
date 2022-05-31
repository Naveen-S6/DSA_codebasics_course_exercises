def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    sort_right = merge_sort(left)
    sort_left = merge_sort(right)

    return merge_two_sorted_array(sort_left,sort_right)

def merge_two_sorted_array(a,b):
    sorted_arr = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_arr.append(a[i])
            i += 1
        else:
            sorted_arr.append(b[j])
            j += 1

    while i < len_a:
        sorted_arr.append(a[i])
        i += 1

    while j < len_b:
        sorted_arr.append(b[j])
        j += 1

    return sorted_arr


if __name__ == "__main__":
    arr = [2,5,64,1,26,4,75,33,65,22,6,23,76,32,200]
    #arr = merge_two_sorted_array(arr1, arr2)
    n = merge_sort(arr)






    print(n)



