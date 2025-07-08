def bubble_sort(arr):
    n=len(arr)
    permutation=True
    while permutation:
        permutation=False



        for i in range(n-1):


            if arr[i] > arr[i +1]:
                arr[i],arr[i+1] =arr[i+1] ,arr[i]
                permutation=True




arr=[12,15,4,1,9,5]
print(arr)
bubble_sort(arr)
print(arr)