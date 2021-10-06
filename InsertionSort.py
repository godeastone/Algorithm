def insertion_sort(arr, n):
    j = len(arr) - n

    if j == 7:
        return arr

    min = 1000000000
    tmp = j

    for i in range(j, len(arr)):
        if arr[i] < min:
            min = arr[i]
            index = i

    tmp2 = arr[j]
    arr[j] = min
    arr[index] = tmp2

    insertion_sort(arr, n-1)
        

def main():
    arr = [9, 8, 1, 7, 5, 3, 2, 6, 4]
    insertion_sort(arr, 9)
    print(arr)

if __name__ == "__main__":
   main()
