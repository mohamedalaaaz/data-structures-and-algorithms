

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2:[ListNode]) ->[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return None
        if list2 is None:
            return None
        else:
            if list1.val < list2.val:
                head = list1
                current = head
                list1 = list1.next
            else:
                head = list2
                current = head
                list2 = list2.next
            while ((list1 is not None) and (list2 is not None)):
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next

                current = current.next
                while (list1 is not None):
                    current.next = list1
                    current = current.next
                    list1 = list1.next
                while (list2 is not None):
                    current.next = list2
                    current = current.next
                    list2 = list2.next
                return head

