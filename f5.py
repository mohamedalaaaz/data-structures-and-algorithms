def merge_two_arrays(a,b):
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


arr = [10,20,30,36]
arr2=[7,11,18,37]

print(merge_two_arrays(arr,arr2))

