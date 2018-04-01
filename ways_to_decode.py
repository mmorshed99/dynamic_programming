#A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Given an encoded message containing digits, determine the total number of ways to decode it.
#
#Example :
#
#Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
#The number of ways decoding "12" is 2.
class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        n = len(A)
        ###count and A don't have same index base (1 vs 0)
        count = [0] * (n+1) 
        count[0] = 1
        count[1] = 1
        if n <=2 and A[0] != '0':
            return count[n-1]
        if A[0] == '0':
            return 0
        for i in range(2,n+1):
           count[i] = 0
           if (A[i-1] > '0'):
               count[i] = count[i-1]
           if (A[i-2] == '1' or (A[i-2] == '2' and A[i-1] < '7') ):
               count[i] += count[i-2]
        return count[n]
