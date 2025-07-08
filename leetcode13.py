class solution:
    def romantoInt(self, s: str) -> int:
        previous_number = 0
        current_number = 0
        integer_number = 0

        for symbol in s:
            if symbol == "I":
                current_number = 1
            elif symbol == "V":
                current_number = 5
            elif symbol == "X":
                current_number = 10
            elif symbol == "L":
                current_number = 50
            elif symbol == "C":
                current_number = 100
            elif symbol == "D":
                current_number = 500
            elif symbol == "M":
                current_number = 1000

            if current_number <= previous_number:
                integer_number = integer_number + current_number
            else:
                integer_number = integer_number - 2 * previous_number + current_number

            previous_number = current_number

        return integer_number


s = "MCMXCIV"

ss=solution()
sss=ss.romantoInt(s)
print(sss)



class Solution:

    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I':  1,
            'IV': 4,
            'V':  5,
            'IX': 10,
            'X':  10,
            'XL': 40,
            'L':  50,
            'XC': 90,
            'C':  100,
            'CD': 400,
            'D':  500,
            'CM': 900,
            'M':  1000
        }
        num = 0
        matched = False
        for idx, c in enumerate(s):

            # This Roman number was matched in previous step, skipp
            if matched is True:
                matched = False
                continue

            # to catch IV, IX, XL, XC, CD, CM
            try:
                couple = c + s[idx + 1]
                if couple in roman_map:
                    num += roman_map[couple]
                    matched = True
                    continue
            except IndexError:
                pass

            # normal Roman number, add
            num += roman_map[c]

        return num


def main() -> int:

    solution = Solution()
    assert solution.romanToInt('III') == 3
    assert solution.romanToInt('LVIII') == 58
    assert solution.romanToInt('MCMXCIV') == 1994

    return 0


if __name__ == "__main__":
    raise SystemExit(main())



