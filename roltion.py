from typing import List

class slotion:

    def roltion(self ,matrix:List[List[int]]):
        l,r=0, len(matrix) -1
        while l < r :
            for i in range(r - l):
                top ,bottom=l,r

                topLeft=matrix[top][l+i]

                matrix[top][l+i]=matrix[bottom -i][i]

                matrix[bottom -i][l] = matrix[bottom][r-i]


                matrix[bottom][r-i] =matrix[top+i][r]
                matrix[top+i][r] =topLeft

            r-=1
            l+=1


matrix=[[1,2,3],[4,5,6],[7,8,9]]

g=slotion()
de=g.roltion(matrix)
print(de)
