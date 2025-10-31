from typing import List

class soultion:

    def twosum(self ,nums :List[int] ,target :int) -> List[int]:
        l,r= 0, len(nums) -1
        while l < r :
            cursum =nums[l] +nums[r]
            if cursum > target:
                r -= 1
            elif cursum < target:
                l +=1
            else:
                return [l+1 ,r+1]


arr=[2,4,7,10,12]
g=11
s=soultion()
pr=s.twosum(arr,g)
print(pr)

print(pr)
