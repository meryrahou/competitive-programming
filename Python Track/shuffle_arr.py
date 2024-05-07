class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        return [elem for i in range(n) for elem in [nums[i], nums[n + i]]]


        