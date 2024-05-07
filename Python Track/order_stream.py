class OrderedStream(object):
    def __init__(self, n):
        self.l = [None] * n
        self.ptr = 0

    def insert(self, idKey, value):
        self.l[idKey - 1 ] = value
        returning_list = []

        while self.ptr < len(self.l) and self.l[self.ptr] is not None:
            returning_list.append(self.l[self.ptr])
            self.ptr += 1

        return returning_list
     


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)