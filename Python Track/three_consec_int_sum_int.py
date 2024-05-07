class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        val = num//3
        while val >= 0 and 3*val == num:
            return [val-1,val,val+1]
        return []