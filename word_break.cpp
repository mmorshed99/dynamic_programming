/*Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
#
#For example, given
#
#s = "myinterviewtrainer",
#dict = ["trainer", "my", "interview"].
#Return 1 ( corresponding to true ) because "myinterviewtrainer" can be segmented as "my interview trainer".
#
#Return 0 / 1 ( 0 for false, 1 for true ) for this problem
*/
bool find (string A, vector<string>B){
    for(int i = 0;i<B.size();i++){
        if(A== B[i]){
            return 1;
        }
    }
    return 0;
}

int Solution::wordBreak(string A, vector<string> &B) {
    int n = A.size();
    vector<int>final(n+1,0);
    final[n] = 1;
    for(int i = n-1; i>=0; i--){
        for(int j = i; j<n;j++){
            string sub = A.substr(i,j-i+1);
            if(find(sub,B) == 1 && final[j+1] == 1){
                final[i] = 1;
                break;
            }
        }
    }
    return final[0];
}
