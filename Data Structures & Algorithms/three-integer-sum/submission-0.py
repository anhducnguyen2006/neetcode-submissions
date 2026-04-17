class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d = {}

        for i in range(len(nums)): 
            for j in range(len(nums)):
                if j != i:
                    if (nums[i]+nums[j]) not in d: 
                        d[nums[i]+nums[j]] = []
                    d[nums[i]+nums[j]].append((i, j))
        
        ret = []
        d2 = {}
        for k in range(len(nums)):
            if (-nums[k]) in d: 
                for i in d[-nums[k]]:
                    if k not in i:
                        temp = [nums[k], nums[i[0]], nums[i[1]]]
                        temp = tuple(sorted(temp))
                        if temp not in d2: 
                            d2[temp] = True
                            ret.append(temp)
        return ret