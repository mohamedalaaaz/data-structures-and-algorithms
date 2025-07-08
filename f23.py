from typing import List

class solution:


    def searchrange(self,num:List[int],target:int) ->List[int]:
        left=self.binarysearch(num,target,True)
        right=self.binarysearch(num,target,False)
        return [left,right]
    def binarysearch(self,num,target,leftBinas):
        l,r=0,len(num)-1
        i=-1
        while l<=r:
            m=(l + r)//2
            if target >num[m]:
                l=m+1
            elif target <num[m]:
                r=m-1
            else:
                i=m
                if leftBinas:
                    r=m-1
                else:
                    l=m+1
        return i

t=2
nums=[2,7,7,8,8,10]


d=solution()
dd=d.searchrange(nums,t)
print(dd)