from collections import defaultdict

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        Loss = defaultdict(lambda: 0)
        answer = [[],[]]
        for i in matches:
            Loss[i[1]] += 1
            Loss[i[0]] += 0

        for key, value in Loss.items():
            if value == 0 : answer[0].append(key)
            if value == 1 : answer[1].append(key)

        return [sorted(answer[0]), sorted(answer[1])]
