class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        largestValue = 0
        currentValue = 0
        largeIndex = 0
        count = 0
        for number in A:            
            currentValue = number
            if currentValue > largestValue:
                largestValue = currentValue
                largeIndex = count
            count+=1
        
        return largeIndex
        
run = Solution()
print(run.peakIndexInMountainArray([1,50,10]))