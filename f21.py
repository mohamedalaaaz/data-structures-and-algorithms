class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class solution:
    def copyrendomlist(self ,head: 'Node') -> 'Node':
        oldtocopy={None:None}


        cur = head
        while cur:
            copy=Node(cur.val)
            oldtocopy[cur] =copy
            cur=cur.next
        cur=head
        while cur:
            copy=oldtocopy[cur]
            copy.next=oldtocopy[cur.next]
            copy.random= oldtocopy[cur.random]
            cur=cur.next
        return oldtocopy[head]



f=[[7,0],[13,0],[11,4],[55,6]]

pr=solution()
pri=pr.copyrendomlist(f)
print(pri)





