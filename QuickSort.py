def swap(a, b):
    return b, a


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r-1):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = swap(A[i], A[j])
    A[r], A[i + 1] = swap(A[r], A[i + 1])

    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

    return A

l = [2, 1, 5, 7, 4, 9, 12, 3]
quicksort(l, 0, 7)
print(l)

