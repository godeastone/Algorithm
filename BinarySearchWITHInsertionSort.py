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


def insertion_sort(arr):
    for n in range(1, len(arr)):
        j = n
        key = arr[j]
        i = j - 1
        index = binary_search(arr, 0, j-1, key)

        # print("j and index : ", j, index + 1)

        for k in range(index, j-1):
            tmp = arr[j]
            arr[j] = arr[k]
            arr[k] = tmp

arr = [9, 8, 1, 7, 5, 3, 2, 6, 4]
insertion_sort(arr)
print(arr)
