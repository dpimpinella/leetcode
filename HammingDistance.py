class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return (bin(x^y).count('1'))


run = Solution().hammingDistance(4,1)
print(run)