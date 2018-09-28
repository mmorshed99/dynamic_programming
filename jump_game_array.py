#Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
#Each element in the array represents your maximum jump length at that position.
#
#Determine if you are able to reach the last index.
#
#For example:
#A = [2,3,1,1,4], return 1 ( true ).
#
#A = [3,2,1,0,4], return 0 ( false ).
#
#Return 0/1 for this problem
#
class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        if len(A) == 0:
            return 1
        if len(A) == 1:
            return 1
            
        save = []
        destin = len(A)-1
        for i in range(0,len(A)):
            save.append(0)
        j = len(A) -2
        for i in range(0,len(A)-1):
           if A[j] >= destin - j :
               save[j] = 1
               destin = j
           j = j-1
        return save[0]
    def canJump1(self, A):
        dest = len(A)-1
        for idx in reversed(range(len(A)-1)):
            if A[idx] >= dest - idx:
                dest = idx
        if dest == 0:
            return 1
        return 0
