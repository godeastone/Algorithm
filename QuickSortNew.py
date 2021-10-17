def swap(a, b):
    return b, a


def partition_new(A, p, r):
    x = A[r]
    i = p - 1
    dup_count = 0

    for j in range(p, r):
        if A[j] < x:
            i = i + 1
            A[i], A[j] = swap(A[i], A[j])
        elif A[j] == x:
            dup_count += 1

    A[r], A[i + 1] = swap(A[r], A[i + 1])

    m = i + 2
    n = i + 2

    while dup_count != 0:
        if A[n] == x:
            A[n], A[m] = swap(A[n], A[m])
            m = m + 1
            n = n + 1
            dup_count -= 1
        else:
            n = n + 1

    return i+1, m-1


def quicksort_new(A, p, r):
    if p < r:
        q, t = partition_new(A, p, r)
        quicksort_new(A, p, q - 1)
        quicksort_new(A, t + 1, r)

    return A


l = [2, 1, 5, 7, 4, 9, 12, 3, 5, 3, 3]
quicksort_new(l, 0, 10)
print(l)

