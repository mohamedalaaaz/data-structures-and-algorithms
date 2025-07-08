def selection_sort(list):
    n= len(list)

    for i in range(n):
        index_min=i

        for j in range(i,n):

            if list[j] <list[index_min]:
                index_min=j
        list[index_min],list[i] =list[i] ,list[index_min]



l=[1,14,9,2,55,66,88]
print(l)
selection_sort(l)
print(l)