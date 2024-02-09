class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
            """
        num_index_dict = {}  
        
        for i, num in enumerate(nums):
            if num in num_index_dict and i - num_index_dict[num] <= k:
                return True  
            num_index_dict[num] = i  
        return False  
