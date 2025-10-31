from typing import List

class soultion:

    def twosum(self ,nums :List[int] ,target :int) -> List[int]:
        pervmap ={} #valu ,index


        for i,n in enumerate(nums):
            diff =target - n
            if diff in pervmap:
                return [pervmap[diff] ,i]

            pervmap[n] =i

arr=[2,7,11,13]
g=18
s=soultion()
pr=s.twosum(arr,g)
print(pr)

print(pr)
