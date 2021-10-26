class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        difference = numRows - 1 + numRows - 2
        print(difference)
        new_str = ''
        k = difference
        while len(new_str) != len(s):
            for i in s:
                print(i)
                print(k)
                print(new_str)
                if k == difference:
                    k = 0
                    new_str = new_str + i
                else:
                    k += 1
            difference = difference - 1

        return new_str


sol = Solution()
print("Solution: " + sol.convert("PAYPALISHIRING", 3))
