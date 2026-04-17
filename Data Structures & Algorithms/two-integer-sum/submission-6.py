class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i, j in enumerate(nums):
            if (target-nums[i]) in dic:
                return sorted([i, dic[target-nums[i]][0]])
            if j not in dic:
                dic[j] = [i]
        
        return [-1, -1]
