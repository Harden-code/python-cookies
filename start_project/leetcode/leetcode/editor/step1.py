class ArrayList:
    def __init__(self,size=5):
        self._size = size
        self._index = 0
        self._arr = [None] * self._size

    def append(self,data):
        if self._index == self._size:
            self._size = self._size * 2
            new_arr = [None] * self._size
            new_arr[:len(self._arr)] = self._arr
            self._arr = new_arr
        self._arr[self._index] = data
        self._index = self._index + 1

    def to_str(self):
        print(self._arr)


a = ArrayList()

for i in range(6):
    a.append(i)

a.to_str()
