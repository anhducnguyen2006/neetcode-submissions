class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l1 = list(nums)
        for i in range(1, len(nums)):
            l1[i] = l1[i] * l1[i - 1]

        l2 = list(nums)
        for i in range(len(nums) - 2, -1, -1):
            l2[i] = l2[i] * l2[i + 1]

        # print(l1)
        # print(l2)

        ret = [1 for _ in range(len(nums))]
        
        ret[len(nums) - 1] = l1[len(nums) - 2]
        ret[0] = l2[1]

        for i in range(1, len(nums) - 1):
                ret[i] = l1[i - 1] * l2[i + 1]
        
        return ret


                