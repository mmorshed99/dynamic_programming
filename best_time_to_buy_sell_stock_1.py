#Say you have an array for which the ith element is the price of a given stock on day i.
#
#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
#Example :
#
#Input : [1 2]
#Return :  1

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 0
        buy = []
        buy.append(0)
        buy.append(A[0])
        for i in range(2,len(A)):
            buy.append(min(buy[i-1],A[i-1]))
        max_profit = A[1] - buy[1]
        if max_profit < 0:
            max_profit = 0
        for i in range(1,len(A)):
            temp = A[i] - buy[i]
            if temp > max_profit:
                max_profit = temp
        return max_profit
