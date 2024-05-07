class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nb_i = 0
        nb_init = 0
        for i in nums:
            if i == 1: nb_i += 1
            elif i == 0:
                nb_init = max(nb_init, nb_i)
                nb_i = 0
        nb_init = max(nb_init, nb_i)
        return nb_init
        