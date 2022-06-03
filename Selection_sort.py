def selection_sort(arr):
    size = len(arr)

    for i in range(size-1):
        min_ind = i

        for j in range(min_ind+1, size):
            if arr[j] < arr[min_ind]:
                min_ind = j
        if i != min_ind:
            arr[i], arr[min_ind] = arr[min_ind], arr[i]


if __name__ == "__main__":
    arr = [23,42,1,43,45,65,76,9,2]
    selection_sort(arr)
    print(arr)
