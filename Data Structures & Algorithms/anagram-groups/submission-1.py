class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs:
            a = []
            for j in i:
                a.append(j)

            t = tuple(sorted(a))

            if t not in dic:
                dic[t] = [i]
            else:
                dic[t].append(i)
        
        ret = []
        for i in dic.values():
            ret.append(i)
        
        return ret