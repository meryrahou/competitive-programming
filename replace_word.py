class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        def wordindict(word , dictionary):
            test = False
            for mot in dictionary:
                if word[:len(mot)] == mot:
                    test = mot
                    break
            return test


        answer = ''
        dictionary.sort()
        sent = sentence.split(' ')
        for word in sent:
            replacement = wordindict(word , dictionary)
            if replacement == False:
                answer = answer + word + ' '
            else:
                answer = answer + replacement + ' '

        return answer[:-1]
            
        