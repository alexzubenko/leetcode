class Solution:
    def find_dups_instring(self, stringg):
        for i in range(len(stringg)):
            for j in range(i+1, len(stringg)):
                if stringg[i] == stringg[j]:
                    return True
        return False

    def find_dups_instring_has_table(self, stringg):
        check = {}
        for i in stringg:
            if i in check:
                check[i] = 1
            else:
                check[i] = 0
        for key in check.keys():
            if check[key] == 1:
                return True
        return False

    def find_dups_remove(self, stringg):
        lenn = len(stringg)
        while lenn:
            if stringg[0] in stringg[0+1:]:
                return True
            else:
                stringg = stringg[0+1:]
                lenn -=1
        return False





sol = Solution()
print(sol.find_dups_instring('toprt'
))
print(sol.find_dups_instring_has_table('toprt'))
print(sol.find_dups_remove('toprt'))
