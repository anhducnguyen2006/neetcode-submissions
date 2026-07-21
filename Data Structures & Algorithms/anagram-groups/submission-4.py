class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {} 
        for i in strs: 
            l = [0] * 26
            for j in i: 
                k = ord(j) - 97
                l[k] += 1
            l = tuple(l)
            if l not in d: 
                d[l] = []
            d[l].append(i)
        
        return list(d.values())
            
