"""
Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,

merge_sort(elements, key='time_hours', descending=True)
This will sort elements by time_hours and your sorted list will look like,

elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
But if you call it like this,

merge_sort(elements, key='name')
output will be,

elements = [
        { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
    ]

"""
def merge_sort(arr, key,desending = False):
    if len(arr) == 1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left, key,desending)
    merge_sort(right, key,desending)

    merge_sorted_arrays(left, right, arr, key,desending)

def merge_sorted_arrays(a, b, arr, key, decending):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if decending:
            if a[i][key] >= b[j][key]:
                arr[k] = a[i]
                i += 1

            else:
                arr[k] = b[j]
                j += 1
            k += 1
        else:
            if a[i][key] <= b[j][key]:
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
    elements = [
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
    ]
    merge_sort(elements,"time_hours",desending=True)
    print(elements)
    merge_sort(elements, "age")
    print(elements)