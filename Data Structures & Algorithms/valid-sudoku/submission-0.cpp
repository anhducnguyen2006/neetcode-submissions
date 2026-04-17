class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        bool ans = true;
        
        for(int i = 0; i < 9; i++) {
            map<char, int> diff_row;
            map<char, int> diff_col;
            for(int j = 0; j < 9; j++) {

                if(board[i][j] != '.') {
                    if(diff_row.count(board[i][j])) {
                        return false;
                    } else {
                        diff_row.insert({board[i][j], 1});
                    }
                }
                if(board[j][i] != '.') {
                    if(diff_col.count(board[j][i])) {
                        return false;
                    } else {
                        diff_col.insert({board[j][i], 1});
                    }
                }
            }
        }
        for(int i = 0; i < 9; i+=3) {
            for(int j = 0; j < 9; j+=3) {
                map<int, int> diff;
                for(int k = 0; k < 3; k++) {
                    for(int l = 0; l < 3; l++) {
                        if(board[i+k][j+l] != '.') {
                            if(diff.count(board[i+k][j+l])) {
                                return false;
                            } else {
                                diff.insert({board[i+k][j+l], 1});
                            }
                        }
                    }
                }
            }
        }


        return ans;
    }
};
