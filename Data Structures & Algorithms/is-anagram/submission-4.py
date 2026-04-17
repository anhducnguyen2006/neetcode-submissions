class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}

        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        print(dic)
        for i in t:
            if i not in dic:
                return False
            else:
                dic[i] -= 1
                print(dic[i])
                if dic[i] < 0:
                    return False
                if dic[i] == 0:
                    del dic[i]
        
        if dic:
            return False
        return True