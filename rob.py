from typing import  List



class soultion:
    def rob(self ,num : List [int] ) -> int:
        rob1,rob2=0,0

        for i in num:
            temp= max(i+rob1 ,rob2)
            rob1 =rob2
            rob2 =temp

        return rob2



f=[1,2,3,1]
s=soultion()
sa=s.rob(f)
print(sa)
