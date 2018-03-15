#Find the longest increasing subsequence of a given sequence / array.
#
#In other words, find a subsequence of array in which the subsequence’s elements are in strictly increasing order, and in which the subsequence is as long as possible.
#This subsequence is not necessarily contiguous, or unique.
#In this case, we only care about the length of the longest increasing subsequence.
#
#Example :
#
#Input : [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
#Output : 6
#
#The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]
#
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        save = []
        for i in range(len(A)):
            save.append(1)
        if len(A) == 0:
            return 0
        final_count = 1
        for i in range(1,len(A)):
            for j in range(0,i):
                if A[i] > A[j]:
                    save[i] = max(save[i],save[j]+1)
            if final_count < save[i]:
                final_count = save[i]
        return final_count
