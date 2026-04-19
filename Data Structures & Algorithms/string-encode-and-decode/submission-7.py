class Solution:
    d = {}
    def encode(self, strs: List[str]) -> str:
        encoded_str = "#".join(strs)
        self.d[encoded_str] = strs
        return encoded_str

    def decode(self, s: str) -> List[str]:
        return self.d[s]