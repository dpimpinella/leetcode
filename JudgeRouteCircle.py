class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        origin = [0,0]
        for char in moves:
            if char == 'U':
                origin[1] += 1
            elif char == 'D':
                origin[1] -= 1
            elif char == 'R':
                origin[0] += 1
            else:
                origin[0] -= 1
        if origin == [0,0]:
            return True
        else:
            return False

run = Solution().judgeCircle('UD')


