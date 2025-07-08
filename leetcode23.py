
def mergeKLists(self, lists):
    if not lists:
        return None

    sentinel = ListNode('0')
    while len(lists) > 1:
        merged = []
        while len(lists) > 1:
            merged.append(self.merge(lists.pop(), lists.pop(), sentinel))
        lists += merged
    return lists[0]


def merge(self, x, y, s):
    current = s
    while x and y:
        if x.val < y.val:
            current.next = x
            x = x.next
        else:
            current.next = y
            y = y.next
        current = current.next
    current.next = x if x else y
    return s.next






"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def MeargeListS(self, List: [ListNode]) -> [ListNode]:
        if not List or len(List) ==0:
            return None
        while len(List) > 1:
            margeList=[]
            for  i  in range(0,len(List),2):
                l1=List[i]
                l2=List[i +1 ] if(i+1) <len(List) else None
                margeList.append(self.margelist(l1,l2))




            List=margeList
        return List[0]
    def margelist(self,l1,l2):
        dummy=ListNode
        tail=dummy
        while l1 and l2 :
            if l1.val <l2.val :
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            if l1 :
                tail.next =l1
            if l2:
                tail.next=l2
        return dummy.next

lists = [[1,4,5],[1,3,4],[2,6]]
dd=Solution()
sss=dd.MeargeListS(lists)
print(sss)

"""