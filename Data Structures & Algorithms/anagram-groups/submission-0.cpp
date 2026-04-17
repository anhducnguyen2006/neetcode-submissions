class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> ans;
        for(auto x : strs) {
            vector<int> temp(26, 0);
            for(auto y : x) {
                int z = y-'a';
                temp[z]++;
            }
            if(ans.count(temp)) {
                ans[temp].push_back(x);
            } else {
                ans.insert({temp, {x}});
            }
        }
        vector<vector<string>> answer;
        for(auto x : ans) {
            answer.push_back(x.second);
        }
        return answer;
    }
};
