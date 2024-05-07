class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        decrease = 0
        for ind in range(len(nums)-1): 
            if nums[ind] > nums[ind+1]:
                decrease += 1
                if ind > 0 and nums[ind+1] < nums[ind-1]:
                    nums[ind+1] = nums[ind]  
                else:
                    nums[ind] = nums[ind+1]  

        return decrease <= 1
