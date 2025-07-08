class nodetree:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None


def pre_order(root):
    if root == None :return
    print(root.value)
    print(root.left)
    print(root.right)


root=nodetree(1)
node1=nodetree(2)
node2=nodetree(3)
node3=nodetree(4)
node4=nodetree(5)
node5=nodetree(6)
root.left =node1
root.right =node2
node2.left=node3
node2.right=node4
node4.left=node5
