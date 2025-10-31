from typing import List

class solution:
    def combintionsum(self,candites:List[int] ,target :int) -> List[List[int]]:
        res=[]
        def dfs( i,cur,total):
            if total == target:
                res.append(cur.copy())
                return

            if i >= len(candites) or total > target:
                return
            cur.append(candites[i])
            dfs(i, cur, total + candites[i])
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        return res







f=[2,3,6,7]
df=7

d=solution()
dd=d.combintionsum(f,df)

print(dd)
