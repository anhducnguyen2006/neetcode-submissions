class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in strs: 
            t = tuple(sorted([x for x in i]))
            if t not in d: 
                d[t] = []
            d[t].append(i)
        
        ret = list(d.values())
        return ret
    