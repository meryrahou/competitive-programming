class Solution(object):
    def wateringPlants(self, plants, capacity):
        """
        :type plants: List[int]
        :type capacity: int
        :rtype: int
        """
        steps = 0
        cap = capacity
        for i in range(-1,len(plants)-1):
            if cap >= plants[i+1]:
                steps += 1
                cap -= plants[i+1]
            else:
                steps += 2 * i + 3
                cap = capacity - plants[i+1]
        return steps
        