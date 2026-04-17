class Solution {
public:
    int hammingWeight(uint32_t n) {
        ios_base::sync_with_stdio(false);
        cin.tie(0);
        int ans = 0; 
        for(int i = 0; i < 32; i++) {
            if((n & (1 << i)) != 0) {
                ans++;
            }
        }
        return ans;
    }
};
