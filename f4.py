def instrtion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j = j - 1
            print(arr)
        # print(arr)




arr = [9, 8, 5, 6, 14, 2]

instrtion_sort(arr)
print(arr)
