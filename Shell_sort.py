def shell_sort(elements):
    size = len(elements)
    gap = size//2

    while gap > 0:
        for i in range(gap,size):
            anchor = elements[i]
            j = i

            while j >= gap and elements[j-gap]>anchor:
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        gap = gap//2

if __name__ == "__main__":
    arr = [21,38,29,17,4,25,11,32,9,2]
    shell_sort(arr)
    print(arr)

