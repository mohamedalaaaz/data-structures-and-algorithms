from  typing import  List

class solution:

    def twosum(self , num:List[int] , target :int) -> List[int]:
        seen={}
        for i  ,value  in enumerate(num):
            re= target -num[i]
            if re  in seen:
                return [i,seen[re]]

            seen[value] =i




d=[5,12,8,9,6,2]

f=0

ko=solution()
do=ko.twosum(d,f)
print(do)
