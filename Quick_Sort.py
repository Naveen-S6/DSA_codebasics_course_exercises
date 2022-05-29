def swap(a, b, ele):
    if a != b:
        temp = ele[a]
        ele[a] = ele[b]
        ele[b] = temp

def partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, arr)

    swap(pivot_index, end, arr)

    return end


def Quick_sort(arr, start, end):

    if start < end:
        pi = partition(arr, start, end)
        Quick_sort(arr, start, pi-1)
        Quick_sort(arr, pi+1, end)

if __name__ == "__main__" :
    arr = [11, 9, 29, 7, 2, 15, 28]
    Quick_sort(arr, 0, len(arr)-1)
    print(arr)



