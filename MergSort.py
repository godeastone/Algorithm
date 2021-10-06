def mergesort(l):
    if len(l) < 2:
        return l

    mid = len(l) // 2
    left = mergesort(l[:mid])
    right = mergesort(l[mid:])

    if left and right:
        return merge(left, right)

def merge(left, right):
    left.append(99999)      # Suppose 99999 is infinite.
    right.append(99999)     # Suppose 99999 is infinite.
    index1 = 0
    index2 = 0
    temp = []

    while left[index1] != 99999 or right[index2] != 99999:
        if left[index1] >= right[index2]:
            temp.append(right[index2])
            index2 += 1
        else:
            temp.append(left[index1])
            index1 += 1
    return temp


l = [38, 27, 43, 3, 9, 82, 10]
result = mergesort(l)
print(result)

