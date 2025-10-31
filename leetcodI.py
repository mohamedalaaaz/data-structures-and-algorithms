def merge_two_list(a,b):
    n=len(a)
    m=len(b)
    i=0
    j=0
    result=[]
    while i < n and j < m:
        if a[i] < b[j]:
            result.append(a[i])
            i+=1
        else:
            result.append(b[j])
            j+=1

    while i <n:
        result.append(a[i])
        i+=1
    while j < m:
        result.append(b[j])
        j+=1
    return result


def merge_sort(arr):
    n=len(arr)
    if n <= 1:
        return arr
    mid=n //2
    a=merge_sort(arr[0 :mid])

    b=merge_sort(arr[mid:n])

    r=merge_two_list(a,b)

    return r


one_list=[14,28,5,66,9,44]
print(merge_sort(one_list))


