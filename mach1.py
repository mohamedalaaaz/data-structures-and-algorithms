class soution1:
    def romansoution(self ,s :str):
        s=s[::-1]
        re=0
        prv=0

        for i in range(len(s)):
            curr=self.get_char(s[i])
            if prv >= curr:
                re -= curr
            else:
                re +=curr
            prv=curr
        return  re

    def get_char(self, char):
        mapping_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        return mapping_roman[char]


g=soution1()

f=g.romansoution('mxx')