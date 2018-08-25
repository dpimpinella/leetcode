class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        #sum up values if both are not None
        if not t1: return t2
        if not t2: return t1
        
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
        
t1 = TreeNode(1)
t1.left = TreeNode(5)
t2 = TreeNode(2)
t2.left = TreeNode(6)

testRun = Solution()
testRun.mergeTrees(t1,t2)