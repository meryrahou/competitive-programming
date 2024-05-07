class FrequencyTracker(object):
    def __init__(self):
        self.arr = []  
        self.freq = defaultdict(int)  

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.freq[number] += 1
        self.arr.append(number)

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.arr:
            self.freq[number] -= 1
            if self.freq[number] == 0:
                del self.freq[number]
            self.arr.remove(number)

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        return frequency in self.freq.values()
