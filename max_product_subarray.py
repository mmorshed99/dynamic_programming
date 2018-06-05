class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        max1 = A[0]
        max2 = A[0]
        mymax = A[0]
        for i in range(1,len(A)):
            if A[i] > mymax:
                mymax = A[i]
            if A[i] == 0:
                max1 = 1
                max2 = 1
            elif A[i] < 0:
                if max2 < 0:
                    max1 = max2 * A[i]
                    max2 = A[i]
                    if max1 > mymax:
                        mymax = max1
                else:
                    if max2 != 0:
                        max2 = max1 * A[i]
                    else:
                        max2 = A[i]
                    max1 = 1
            else:
                if max1 <= 0:
                    max1 = A[i]
                    if max1 != 0:
                        max2 = max2 * A[i]
                else:
                    max1 = max1 * A[i]
                    max2 = max2 * A[i]
                if max1 > mymax:
                    mymax = max1
        return mymax
