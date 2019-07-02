'''Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.'''


class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        x = 0
        while x < len(s):
            y = 1
            if s[x] == "I":
                if x + 1 < len(s):
                    nextNumber = s[x + 1]
                    if nextNumber == "V":
                        number = number + 4
                        y = 2
                    elif nextNumber == "X":
                        number = number + 9
                        y = 2
                    else:
                        number = number + 1
                else:
                    number = number + 1
            if s[x] == "V":
                number = number + 5
            if s[x] == "X":
                if x + 1 < len(s):
                    nextNumber = s[x + 1]
                    if nextNumber == "L":
                        number = number + 40
                        y = 2
                    elif nextNumber == "C":
                        number = number + 90
                        y = 2
                    else:
                        number = number + 10
                else:
                    number = number + 10
            if s[x] == "L":
                number = number + 50
            if s[x] == "C":
                if x + 1 < len(s):
                    nextNumber = s[x + 1]
                    if nextNumber == "D":
                        number = number + 400
                        y = 2
                    elif nextNumber == "M":
                        number = number + 900
                        y = 2
                    else:
                        number = number + 100
                else:
                    number = number + 100
            if s[x] == "D":
                number = number + 500
            if s[x] == "M":
                number = number + 1000
            x = x + y
        return number


solution = Solution()
print(solution.romanToInt(s="MCMXCIV"))
