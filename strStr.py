class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        else:
            for r in range(len(haystack) - len(needle) + 1):
                s = haystack[r:r + len(needle)]
                if needle == s:
                    return r
            return -1


sol = Solution()
print(sol.strStr("hello", "lel"))
