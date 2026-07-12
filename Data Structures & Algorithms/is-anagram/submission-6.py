class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0] * 26

        for i in s: 
            l[ord(i) - 97] += 1
        
        for i in t: 
            l[ord(i) - 97] -= 1

        if any(l): 
            return False
        return True