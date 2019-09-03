class Solution:
    def find_dups_instring(self, stringg):
        for i in range(len(stringg)):
            for j in range(i+1, len(stringg)):
                if stringg[i] == stringg[j]:
                    return True
        return False





sol = Solution()
print(sol.find_dups_instring('trao'
))