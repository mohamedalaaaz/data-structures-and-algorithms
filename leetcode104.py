class ListNode:
    def __init__(self, val=0,right=None, left=None):
        self.val = val
        self.left = left
        self.right=right



class Solution:
    def inverttree(self,root :ListNode):



        stack=[[root,1]]
        res=1
        while stack:
            node,debth=stack.pop()
        if node :
            res=max(res,debth)
            stack.append([node.right,debth+1])
            stack.append([node.left, debth + 1])

        return res

root=[3,9,20,5,8,15,7]
dd=Solution()
dds=dd.inverttree(root)
print(dds)