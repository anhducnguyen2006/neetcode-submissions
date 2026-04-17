class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}

        for i in nums:
            d[i] = True
        
        ret = 0
        for i in d: 
            k = 1
            while (i+k) in d:
                k += 1
            ret = max(ret, k)
        return ret

            
        
