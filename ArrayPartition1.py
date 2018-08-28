class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sortedNums = sorted(nums)
        sumOfMins = 0
        while len(sortedNums) >= 2:
            pair = [sortedNums.pop(0), sortedNums.pop(0)]
            sumOfMins += min(pair)
        return sumOfMins




test = [1,7,4,5]
run = Solution().arrayPairSum(test)
print(run)