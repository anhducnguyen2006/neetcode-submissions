class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = [0 for _ in range(26)]

        for i in s: 
            a[ord(i) - 97] += 1
        
        for i in t:
            temp = ord(i) - 97
            a[temp] -= 1
            if a[temp] < 0: 
                return False
        
        if sum(a) == 0:
            return True
        return False

