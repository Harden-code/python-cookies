import multiprocessing as mp


def echo(i):
    print('1',i)
    return i


if __name__ == '__main__':
    with mp.Pool(8) as pool:
        r = pool.map(echo,[1])

print('cpu count',mp.cpu_count())
