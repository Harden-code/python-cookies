import time
from queue import Queue
from threading import *
from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float


# c1 = Coordinate('2', 3)

class DemoClass:
    a: int
    b: float = 1.1
    c = 'span'


print(DemoClass.__annotations__)
# print(DemoClass.a)
d = DemoClass()
print(d.b)


class BlockQueue:

    def __init__(self, size):
        self._queue = []
        self._size = size
        self._condi = Condition()

    def push(self, ele):
        with self._condi:
            while len(self._queue) == self._size:
                print('push wait')
                self._condi.wait()
            self._queue.append(ele)
            self._condi.notify_all()

    def poll(self):
        with self._condi:
            while len(self._queue) == 0:
                self._condi.wait()
            self._condi.notify_all()
            print('poll')
            return self._queue.pop()


b = BlockQueue(2)


def show_pop(queue):
    time.sleep(3)
    queue.poll()
    print('end')


t1 = Thread(target=show_pop, args=[b])

b.push(1)
b.push(2)
t1.start()
b.push(3)

print('t1 start')
print('2')
