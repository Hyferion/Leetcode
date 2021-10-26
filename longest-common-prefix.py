class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        prefix = ''

        for i in range(len(strs[0])):
            pre = strs[0][i]
            add = False
            for word in strs:
                try:
                    if pre != word[i]:
                        return prefix
                    else:
                        add = True
                except IndexError:
                    return prefix
            if add:
                prefix = prefix + pre

        return prefix




sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))