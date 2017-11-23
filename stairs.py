#You are climbing a stair case. It takes n steps to reach to the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
#Example :
#
#Input : 3
#Return : 3
#
#Steps : [1 1 1], [1 2], [2 1]
#
#
class Solution:
    # @param A : integer
    # @return an integer
    def climbStairs(self, A):
     n = A
     save = []
     if n == 1:
         return 1
     if n == 2:
         return 2
     if n == 3:
         return 3
     for i in range(0,n+1):
        save.append(0)
     save[1] = 1
     save[2] = 2
     save[3] = save[1]+save[2]
     i = 4
     while(i<n+1):
         save[i]	= save[i-1] + save[i-2] 
         i+= 1
     return save[n]    
