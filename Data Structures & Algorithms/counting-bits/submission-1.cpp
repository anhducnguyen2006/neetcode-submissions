
class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> v(n+1, 0);
        for(int i = 0; i <= n; i++) {
            int j = i;
            while(j) {
                v[i] += (j & 1);
                j >>= 1;
            }

        }
        return v;
    }
};
