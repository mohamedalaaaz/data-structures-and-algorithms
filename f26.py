from typing import List
import collections

class solution:
    def maxsilidingwindow(self,nums:List[int],k:int) ->List[int]:
        output=[]
        q=collections.deque()
        l=r=0
        while r < len(nums):
            while q and nums[q[-1]] <nums[r]:
                q.pop()
            q.append(r)
            if l >q[0]:
                q.popleft()
            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1
            r+=1

        return output

l=[1,-3,-1,-3,5,6,7]
t=5
d=solution()
dd=d.maxsilidingwindow(l,t)
print(dd)

