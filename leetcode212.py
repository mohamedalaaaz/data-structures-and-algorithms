from  typing import  List

class TrieNode:
    def __init__(self):
        self.children={}
        self.isword=False


    def addword(self,word):
        cur=self
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.isword=True


class solution:
    def foundwords(self,board:List[List[str]] ,words:List[str]):
