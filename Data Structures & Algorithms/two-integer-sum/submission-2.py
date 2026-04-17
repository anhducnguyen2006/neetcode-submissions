class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]] = []
                d[nums[i]].append(i)
            else:
                d[nums[i]].append(i)
        print(d)
        for key, val in d.items():
            if (target-key) in d.keys():
                if (target-key) == key:
                    if(len(val) > 1):
                        return [val[0], val[1]]
                    else:
                        continue
                else:
                    return [val[0], d[target-key][0]]
        return []
