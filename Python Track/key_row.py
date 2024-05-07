class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        answer = []

        for word in words:
            wordlower = word.lower()
            if all(char in row1 for char in wordlower) or all(char in row2 for char in wordlower) or all(char in row3 for char in wordlower):
                answer.append(word)

        return answer
