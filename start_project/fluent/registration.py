regis = []


# 装饰器函数返回值必须是可调用的
def wrap_func(func):
    print('doing wrap_func')
    regis.append(func)
    return func


@wrap_func
def f1():
    print('f1')


@wrap_func
def f2():
    print('f2')


def main():
    print('main')
    print('regis->',regis)
    # f2()


if __name__ == '__main__':
    main()
