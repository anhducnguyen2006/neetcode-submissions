class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ret = 0

        l, r = 0, len(heights) - 1
        while l < r: 
            s = (r-l)
            if heights[l] < heights[r]:
                s *= heights[l]
                l += 1 
            else: 
                s *= heights[r]
                r -= 1
            ret = max(ret, s)
        
        return ret
            
            
