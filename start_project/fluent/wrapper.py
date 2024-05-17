# import registration
import sys
from itertools import cycle
arr = []


def wrap(func):
    print(arr)

    def inner():
        func()

    return inner


def wrap_arg(msg):
    print('wrap_arg', msg)

    def foo(func):
        print('foo')
        return func

    return foo


@wrap
def f1():
    print('f1')


@wrap
def f2():
    print('f1')


# wrap_arg() 调用该函数,返回一个 def wrap_factory(func:callable)->callable
@wrap_arg('ll')
def f3(func: callable) -> callable:
    func()
    print('f3')


f3(f2)
# from dis import dis

# print(dis(wrap))
# print(f1)


def spin(i):
    for s in cycle(['\\', '|', '/']):

        print(s, file=sys.stdout)
        sys.stdout.flush()
        import time
        time.sleep(1)
        i -= 1
        if not i:
            break


spin(10)
