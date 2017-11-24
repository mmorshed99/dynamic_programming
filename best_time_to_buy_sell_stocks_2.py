#Best Time to Buy and Sell Stocks IIBookmark Suggest Edit
#Say you have an array for which the ith element is the price of a given stock on day i.
#
#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
#Example :
#
#Input : [1 2 3]
#Return : 2
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if len(A) == 0:
            return 0
        if len(A) == 1:
            return 0
        total = 0
        for i in range(1,len(A)):
            curr = A[i] - A[i-1]
            if curr>0:
                total += curr
        return total
