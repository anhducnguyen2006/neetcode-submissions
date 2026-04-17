class Solution {
public:
    vector<int> key;
    string encode(vector<string>& strs) {
        string ans = "";
        for(auto x : strs) {
            ans += x;
            key.push_back(x.size());
        }
        return ans;
    }

    vector<string> decode(string s) {
        vector<string> ans; int temp = 0, curr = 0;
        for(auto x : key) {
            ans.push_back(s.substr(temp, x));
            temp += x;
        }
        return ans;
    }
};
