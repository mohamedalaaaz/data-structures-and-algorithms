class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        arr = []
        for i, num in enumerate(nums):
            arr.append([i, num])
        i, j = 0, len(arr) - 1
        while i < j:
            sums = arr[i][1] + arr[j][1]
            if sums == target:
                return [arr[i][0], arr[j][0]]
            if sums > target:
                j = j - 1
            else:
                i = i + 1



d=[2,7,11,15]

        arr.sort(key=lambda x: x[1])
        ans = []
f=9
do=Solution()
fp=do.twoSum(d,f)
print(fp)
