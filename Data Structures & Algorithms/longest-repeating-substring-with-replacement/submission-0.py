class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        max_freq = 0
        l = 0
        
        for r, c in enumerate(s):
            dic[c] = 1 + dic.get(c, 0)

            max_freq = max(max_freq, dic[c])

            if r - l + 1 - max_freq > k:
                dic[s[l]] -= 1
                l += 1

        return len(s) - l