class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        xcount = 0
        ycount = 0
        for char in moves:
            if char == 'U':
                ycount += 1
            elif char == 'D':
                ycount -= 1
            elif char == 'R':
                xcount += 1
            else:
                xcount -= 1
        if ycount == 0 and xcount == 0:
            return True
        else:
            return False
run = Solution().judgeCircle('LL')


