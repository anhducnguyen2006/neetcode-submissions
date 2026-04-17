class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(31, -1, -1):
            if n & (1 << i) != 0:
                ret |= (1 << (31-i))
        return ret
            