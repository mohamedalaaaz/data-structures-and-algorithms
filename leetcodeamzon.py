class ListNode:
    def __init__(self, x):
        self.val=x
        self.left=None
        self.right=None



class Solution:
    def addTwoNumbers(self, root: "ListNode", l1: "ListNode",l2 :"ListNode"):
        cur=root
        while cur :
            if l1.val >cur.val and l2.val >cur.val:
                cur=cur.right
            elif l1.val <cur.val and l2.val <cur.val:
                cur=cur.left
            else:
                return  cur