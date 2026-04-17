class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1 = [None for _ in range(len(nums))]
        l2 = [None for _ in range(len(nums))]
        for i in range(1, len(nums)):
            l1[i] = nums[i-1]
            if l1[i-1] != None:
                l1[i] *= l1[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            l2[i] = nums[i+1]
            if l2[i+1] != None:
                l2[i] *= l2[i+1]

        print(l1, l2)

        ret = []
        for i, j in zip(l1, l2):
            if i != None and j != None:
                ret.append(i * j)
            elif i == None and j != None:
                ret.append(j)
            elif i != None and j == None:
                ret.append(i)
            else:
                ret.append(0)

        return ret