class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        def mymaxProfit(curr_profit,curr_buy,curr_sale,new_sale):
          if curr_sale < curr_buy:
            curr_buy = curr_sale
          if new_sale-curr_buy > curr_profit:
            return new_sale-curr_buy,curr_buy
          else:
            return curr_profit,curr_buy
        def mymaxProfit2(curr_profit,curr_buy,curr_sale,new_buy):
          if curr_buy>curr_sale:
            curr_sale = curr_buy
          if curr_sale - new_buy > curr_profit:
            return curr_sale - new_buy,curr_sale
          else:
            return curr_profit,curr_sale
        length = len(A)
        if length == 0 or length ==1:
           return 0
        if length == 2:
          if A[1]-A[0]>0:
            return A[1]-A[0]
          else:
            return 0
        forward = []
        backward = []
        forward.append(0)
        forward.append(A[1]-A[0])
        curr_buy = A[0]
        curr_profit = A[1]-A[0]
        for i in range(2,length):
           curr_profit,curr_buy = mymaxProfit(curr_profit,curr_buy,A[i-1],A[i])
           forward.append(curr_profit)
        j = length-3
        for i in range(0,length):
           backward.append(0)
        curr_profit = A[length-1]-A[length-2]
        if curr_profit < 0:
           curr_profit = 0
        backward[length-2] = curr_profit
        curr_sale = A[length-1]
        for i in range(2,length):
            curr_profit,curr_sale = mymaxProfit2(curr_profit,A[j+1],curr_sale,A[j])
            backward[j] = curr_profit
            j = j-1
        maximum = backward[len(backward)-1]
        for i in range(0,len(forward)):
            if i != len(forward)-1:
                temp = forward[i]+ backward[i+1]
                if temp>maximum:
                    maximum = temp
        if forward[len(forward)-1] > maximum:
            maximum = forward[len(forward)-1]
        return maximum
