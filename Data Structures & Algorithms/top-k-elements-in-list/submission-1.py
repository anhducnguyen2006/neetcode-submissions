class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        ans = [[] for i in range(len(nums)+1)]
        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
        for key, val in dic.items():
            ans[val].append(key)
        final = []
        for i in range(len(ans)-1,0,-1):
            for x in ans[i]:
                final.append(x)
                if len(final) == k:
                    return final
        return []