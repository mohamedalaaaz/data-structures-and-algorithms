from  typing import List
class sloution:
    def findmidiansortedarray(self,num1:List[int],num2:List[int]):
        a,b=num1,num2
        total=len(a)+len(b)
        half=total//2
        if len(b) < len(a):
            a,b=b,a
        l,r=0,len(a)-1
        while True  :
            i=(l+r) //2 #A
            j=half -i -2 #B
            Aleft=a[i] if i >= 0  else float("-infinity")
            Aright=a[i+1] if ( i + 1 ) <len(a) else("infinity")
            Bleft=b[j] if j >= 0 else float("-infinity")
            Bright = b[j + 1] if (j + 1) < len(b) else ("infinity")

            if Aleft <=Bright and Bleft <=Aright:
                #odd
                if total %2:
                    return  min(Aright,Bleft)
                return (max(Aleft,Bleft) +min(Aright,Bright)) /2
            elif Aleft < Bright:
                r=i-1
            else:
                l=i+1



num1=[1,3,4,5,6,7]
num2=[1,2,3,4]


pr=sloution()
prr=pr.findmidiansortedarray(num1,num2)
print(prr)

