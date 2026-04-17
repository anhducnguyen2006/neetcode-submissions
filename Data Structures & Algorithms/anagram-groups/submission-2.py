class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}

        for i in strs: 
            s = [0 for _ in range(26)]

            for j in i: 
                s[ord(j) - 97] += 1
            
            t = tuple(s)
            if t not in dic: 
                dic[t] = []
                dic[t].append(i)
            else:
                dic[t].append(i)
        
        return list(dic.values())
            
    