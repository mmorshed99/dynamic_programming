#Given A, how many structurally unique BST’s (binary search trees) that store values 1...A?
#
#Example :
#
#Given A = 3, there are a total of 5 unique BST’s.
#
#
#   1         3     3      2      1
#    \       /     /      / \      \
#     3     2     1      1   3      2
#    /     /       \                 \
#   2     1         2                 3
#
class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        def my_tree_num(A,save):
            if save[A] != -1:
                return save[A]
            if A == 1:
                save[1] = 1 
                return save[1]
            if A == 2:
                save[2] = 2
                return save[2]
            temp = 0
            for i in range(1,A+1):
                if i == 1:
                    my_left = 1
                    my_right = my_tree_num(A-i,save)
                elif i ==A:
                    my_left = my_tree_num(i-1,save)
                    my_right = 1
                else:
                    my_left = my_tree_num(i-1,save)
                    my_right = my_tree_num(A-i,save)
                temp += my_left * my_right
            save[A] = temp
            return save[A]
        
        save = []
        if A == 1:
            return 1
        for i in range(A+1):
            save.append(-1)
        my_return = 0
        for i in range(1,A+1):
            if i == 1:
                temp_l = 1
                temp_r = my_tree_num(A-i,save)
            elif i == A:
                temp_l = my_tree_num(i-1,save)
                temp_r = 1
            else:
                temp_l = my_tree_num(i-1,save)
                temp_r = my_tree_num(A-i,save)
            my_return += temp_l * temp_r
        return my_return
