class solution:
    def validtree(self,n,edgs):
        if not n:
            True

        adj={i:[] for i in  range(n)}
        for n1 ,n2 in edgs:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit=set()
        def dfs(i,prev):
            if i in  visit:
                return False

            visit.add(i)

            for j in adj[i]:
                if j ==prev:
                    continue
                if not dfs(j,i):
                    return False
            return True
        return dfs(0,-1) and n ==len(visit)







n=5
edges=[[0,1],[0,2],[0,3],[1,4]]

ss=solution()
ssss=ss.validtree(n,edges)
print(ssss)