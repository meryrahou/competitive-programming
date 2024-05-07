class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        w1 = ''.join(w for w in word1)
        w2 = ''.join(w for w in word2)
        return w1 == w2        