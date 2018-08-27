class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """        
        selfDividingNumbersList = []
  

        for num in range(left, right +1):
                isDivisible = True
                for digit in str(num):
                    if digit == '0':
                        isDivisible = False
                        break
                    if num % int(digit) != 0:
                        isDivisible = False
                if isDivisible:
                    selfDividingNumbersList.append(num)
        return selfDividingNumbersList
                    

print(Solution().selfDividingNumbers(15,90))