class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}

        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        l = sorted(dic.items(), key= lambda x: x[1] ,reverse=True)

        ret = []
        for i in range(k):
            ret.append(l[i][0])

        return ret