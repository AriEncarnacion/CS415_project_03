# Mock arrays

maxCapacity = 26
v = [24, 13, 23, 15, 16]
w = [12, 7, 11, 8, 9]
t = [74, 42, 68, 28, 57, 99, 78, 86, 10, 46, 94, 8, 63, 14, 2, 93, 67, 98, 18, 38, 27, 99, 88, 54, 83]

# Returns array of (vi/wi) ratios
def get_ratios(arr_v, arr_w):
    r = []
    i = 0
    while i < len(arr_v):
        r.append(arr_v[i] / arr_w[i])
        i += 1
    return r

# Returns new sorted array
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))


# Helper fn: Returns single sorted array
def merge(larr, rarr):
    merged = []
    i, j = 0, 0

    while i < len(larr) and j < len(rarr):
        if larr[i] > rarr[j]:               # Use '<' for ascending, '>' for descending
            merged.append(larr[i])
            i += 1
        else:
            merged.append(rarr[j])
            j += 1

    if i == len(larr):
        merged += rarr[j:]
    if j == len(rarr):
        merged += larr[i:]

    return merged


#get_ratios(v, w)
print(t)
m = merge_sort(t)

print(m)
print(t)