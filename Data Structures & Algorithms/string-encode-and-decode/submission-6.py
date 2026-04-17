class Solution:

    def encode(self, strs: List[str]) -> str:
        l = []
        for i in strs:

            if i == "":
                l.append('404')
                continue

            temp = []
            for j in i:
                temp.append(ord(j))
            stemp = ','.join(list(map(str, temp)))
            l.append(stemp)
        
        return ';'.join(l)

            

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
            
        ret = []

        l = s.split(';')
        for i in l:
            s = ""
            temp = i.split(',')
            for j in temp:
                if j != '404':
                    s += chr(int(j))
            ret.append(s)

        return ret
            