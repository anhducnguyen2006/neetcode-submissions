class Solution:
    def countBits(self, n: int) -> List[int]:
        ret = [0] * (n+1)

        for i in range(n+1):
            count = 0
            for j in range(32):
                if i & (1 << j) != 0:
                    count += 1
            ret[i] = count
        return ret