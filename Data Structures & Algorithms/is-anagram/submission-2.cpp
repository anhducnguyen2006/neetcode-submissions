class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> m;
        for(auto x : s) {
            if(m.count(x)) {
                m[x]++;
            } else {
                m.insert({x, 1});
            }
        }
        for(auto x : t) {
            if(m.count(x)) {
                if(m[x] - 1 >= 0) {
                    m[x]--;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        int sum = 0;
        for(auto x : m) {
            sum += x.second; 
        }
        return sum ? false : true;
    }
};
