class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0

        d = {}
        start = 0

        for j, i in enumerate(s):
            if i in d and d[i] >= start:
                start = d[i] + 1
            d[i] = j

            ret = max(ret, j - start + 1)
        
        return ret