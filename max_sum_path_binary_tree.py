# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        def my_max_path(A,curr_max):
            if A == None:
                return 0,curr_max
            A_l,curr_max = my_max_path(A.left,curr_max)
            A_r,curr_max = my_max_path(A.right,curr_max)
            branch_max = max(A_l,A_r)
            local_max = max(A.val+branch_max,A.val)
            curr_total = A_l+A.val+A_r
            max_now = max(local_max,curr_total)
            curr_max = max(curr_max,max_now)
            return local_max,curr_max
        if A == None:
            return 0
        curr_max = -9999999999
        temp,curr_max = my_max_path(A,curr_max)
        return curr_max
