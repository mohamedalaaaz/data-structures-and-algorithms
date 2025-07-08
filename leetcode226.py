class ListNode:
    def __init__(self, val=0,right=None, left=None):
        self.val = val
        self.left = left

        self.right=right



class Solution:
    def inverttree(self,root :ListNode):

        if not root:
            return None


        tmp=root.left
        root.left=root.right
        root.right=tmp

        self.inverttree(root.left)
        self.inverttree(root.right)
        return root