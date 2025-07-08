from typing import List
class solution:
    def jumpII(self,nums:List[int]) ->int:
        res=0
        l=r=0

        while r <len(nums) -1:
            farthest=0
            for i in range(l,r+1):
                farthest=max(farthest,i+nums[i])
            l=r +1
            r=farthest
            res +=1
        return res

nums=[2,2,1,1,4]
d=solution()
dd=d.jumpII(nums)
print(dd)