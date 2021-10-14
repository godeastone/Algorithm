def binary_search(A, low, high, key):
    if high > low:
        mid = (high + low) // 2

        if A[mid] == key:
            return mid

        elif A[mid] > key:
            return binary_search(A, low, mid - 1, key)

        else:
            return binary_search(A, mid + 1, high, key)

    elif high == low:
        if A[low] > key:
            return low
        else:
            return low + 1

    else:
        return low

l = [2, 3, 5, 7, 8, 9, 12]
print(binary_search(l, 0, 6, 6))