class Solution:
    def longestCommonPrefix(self, strs):
        result = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result
        # print(result)
    
    
x= Solution()
x.longestCommonPrefix(["flower","flow","flight"])

#################################################
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in strs: #this loop is for minimum lenghth of string
            if (len(i)<len(prefix) or prefix == ''):
                prefix = i

        need = len(strs)
        count=0
        result = ''
        while(need!=count):
            count = 0
            for i in strs:
                if(prefix == i[:len(prefix)]):
                    count +=1
            result = prefix
            prefix= prefix[:-1]
        if(need==count):
            return result
        else:
            return ''