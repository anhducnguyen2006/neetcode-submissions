class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans(n, 0);
        int curr = nums[0]; ans[1] = curr;
        for(int i = 1; i < nums.size()-1; i++) {
            curr *= nums[i];
            ans[i+1] = curr;
        }
        curr = nums[nums.size()-1]; ans[nums.size()-2]*=curr;
        for(int i = nums.size()-2; i > 0; --i) {
            curr *= nums[i];
            ans[i-1] *= curr;
        }
        ans[0] = curr;
        return ans;
    }
};
