class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        minm = n // 3

        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        result = [num for num, count in count_dict.items() if count > minm]

        return result
