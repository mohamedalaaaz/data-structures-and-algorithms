from typing import List
class solution:
    def spiletarray(self,num:List[int],t:int):
        def canSpilt(largest):
            subarry=0
            cursum=0
            for n in num:
                cursum += n
                if cursum >largest:
                    subarry+=1
                    cursum=n
            return  subarry +1 <=t
        l,r=max(num) ,sum(num)
        res=r
        while l <= r:
            mid =l +((r-l)//2)
            if (canSpilt(mid)):
                res=mid
                r=mid-1
            else:
                l=mid+1

        return  res





nums=[7,2,5,10,8]
n=2

dd=solution()
ssss=dd.spiletarray(nums,n)
print(ssss)