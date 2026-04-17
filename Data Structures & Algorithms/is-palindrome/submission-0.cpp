class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = s.size()-1; bool ok = true;
        while(i <= j) {
            ok = true;
            if(!isalnum(s[i])) {
                i++;
                ok = false;
            }
            if(!isalnum(s[j])) {
                j--;
                ok = false;
            }
            if(ok == true) {
                if(tolower(s[i]) != tolower(s[j])) {
                    return false;
                } else {
                    i++; j--;
                }
            }

        }
        return true;
    }
};
