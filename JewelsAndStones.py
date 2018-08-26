class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0

        for jewel in J:
            for stone in S:
                if jewel == stone:
                    ans += 1

        return ans

run = print(Solution().numJewelsInStones("aA","aAAbbbb"))