def FindMaximumSubarray(A, low, high):
    if high < low:
        return 0, 0, 0

    if high <= low:
        return low, high, A[low]

    else:
        mid = (low + high) // 2
        (left_low, left_high, left_sum) = FindMaximumSubarray(A, low, mid - 1)
        (right_low, right_high, right_sum) = FindMaximumSubarray(A, mid + 1, high)
        (cross_low, cross_high, cross_sum) = FindMaxCrossingSubarray(A, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

def FindMaxCrossingSubarray(A, low, mid, high):
    left_sum = 0
    right_sum = 0
    max_left = 0
    max_right = 0
    flag_left = True
    flag_right = True

    sum = 0
    for i in range(mid - 1, low - 1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
            flag_left = False

    sum = 0
    for j in range(mid + 1, high + 1, 1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
            flag_right = False

    if flag_left:
        max_left = mid
    if flag_right:
        max_right = mid

    return max_left, max_right, left_sum + right_sum + A[mid]


A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(FindMaximumSubarray(A, 0, 8))
