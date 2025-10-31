from typing import List
class slotion:
    def generateparent(self ,n:int) -> List[str]:

        stack=[]
        res=[]

        def bactarck(openN,closed):
            if openN == closed ==n:
                res.append("".join(stack))
                return
            if openN <n:
                stack.append("[")
                bactarck(openN+1,closed)
                stack.pop()
            if closed <openN:
                stack.append("]")
                bactarck(openN,closed+1)
                stack.pop()

        bactarck(0,0)
        return res




j=3
g=slotion()
gg=g.generateparent(j)


print(gg)


