class Solution(object):
    def mergeAlternately(self, word1, word2):
        s=''
        minimum = min(len(word1), len(word2))
        for i in range(minimum):
            s += word1[i] + word2[i]
        
        s += word1[minimum:] + word2[minimum:]

        return s


        