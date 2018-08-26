class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        image = []
        

        for row in A:
            row.reverse()
            element = []
            for num in row:

                if num == 1:
                    element.append(0)
                else:
                    element.append(1)
                
            image.append(element)

        return image

run = Solution().flipAndInvertImage([[1,0,1], [0,1,0], [1,1,0],[0,0,1]])
print(run)

