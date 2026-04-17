class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> m;
        for(auto x : nums) {
            if(m.count(x)) {
                m[x]++;
            } else {
                m.insert({x, 1});
            }
        }
        vector<pair<int, int>> ans;
        for(auto x : m) {
            ans.push_back({x.second, x.first});
        }
        sort(ans.rbegin(), ans.rend());
        vector<int> answer;
        for(int i = 0; i < k; i++) {
            answer.push_back(ans[i].second);
        }
        return answer;
    }
};
