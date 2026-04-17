class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret = 0

        temp = ""
        for i in s:
            if i in temp:
                temp = temp[(temp.find(i)+1):]
            temp += i

            ret = max(ret, len(temp))
        
        return ret