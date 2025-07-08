from typing import List
class solution:

    def longestincrasepath(self,matrix:List[List[int]]):

        rows,cols=len(matrix) ,len(matrix[0])
        dp={}
        def dfs(r,c ,prevVal):
            if (r <0 or r ==rows or
            c <0 or c ==cols or
            matrix[r][c] <=prevVal):
                return 0
            if(r,c) in dp:
                return dp[r,c]
            res=1
