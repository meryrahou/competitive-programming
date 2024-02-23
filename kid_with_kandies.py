class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        greatest = max(candies) - extraCandies
        answer = []
        for candy in candies:
            if candy >= greatest:
                answer.append(True)
            else:
                answer.append(False)

        return answer
                

        