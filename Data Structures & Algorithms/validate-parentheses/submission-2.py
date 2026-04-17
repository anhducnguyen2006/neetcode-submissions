class Solution:
    def isValid(self, s: str) -> bool:
        d = {'[':']', '{':'}', '(':')'}
        
        if len(s) == 1 or s[0] in d.values():
            return False

        stack = []

        stack.append(s[0])

        i = 1
        while i < len(s):
            if s[i] in d:
                stack.append(s[i])
            if s[i] in d.values():
                if not stack:
                    return False
                x = stack.pop()
                if d[x] != s[i]:
                    return False
            i += 1
        
        if stack:
            return False
        return True

