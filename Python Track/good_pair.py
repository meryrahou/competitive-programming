class Solution(object):
    def numIdenticalPairs(self, nums):
        cpt = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i<j:
                    cpt = cpt + 1
        return cpt
        