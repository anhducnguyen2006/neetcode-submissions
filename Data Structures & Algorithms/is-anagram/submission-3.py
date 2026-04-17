class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        for i in t:
            if i in dic.keys():
                if dic[i] > 0:
                    dic[i] -= 1
                    if dic[i] == 0:
                        dic.pop(i)
                else:
                    return False
            else:
                return False
        if bool(dic):
            return False
        else:
            return True
            