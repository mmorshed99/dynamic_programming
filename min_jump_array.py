class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        n = len(A)
        if (n <= 1): 
            return 0
        if (A[0] == 0): 
            return -1
        maxReach = A[0] 
        step = A[0] 
        jump =1
        for i in range(1,n): 
            if (i == n-1): 
                return jump 
            maxReach = max(maxReach, i+A[i])
            step -= 1
            if (step == 0):
                jump += 1
                if(i >= maxReach): 
                    return -1
                step = maxReach - i;
        return -1
