class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        sumdict = {}
        
        common = set(list1) & set(list2)

        for com in common:
            sumdict[com] = list1.index(com) + list2.index(com)

        minimum = min(sumdict.values())

        for key, val in sumdict.items():
            if val == minimum:
                res.append(key)

        return res
