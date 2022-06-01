def shell_sort_remove_duplicates(elements):
    size = len(elements)
    gap = size//2

    while gap > 0:
        index_delete = []
        for i in range(gap, len(elements)):
            anchor = elements[i]
            j = i

            while j >= gap and elements[j-gap] >= anchor:
                if elements[j - gap] == anchor:
                    index_delete.append(j)
                elements[j] = elements[j-gap]
                j -= gap
            elements[j] = anchor
        ind = list(set(index_delete))
        if ind:
            for k in ind:
                del elements[k]
        gap = gap//2

if __name__ == "__main__":
    arr = [0,25,38,29,2,17,0,4,25,11,32,9,9,2]
    shell_sort_remove_duplicates(arr)
    print(arr)

