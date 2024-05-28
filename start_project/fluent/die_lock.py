import threading
import time


def die_lock(left_lock, right_lock):
    with left_lock:
        print(f'step1 lock->{left_lock}')
        time.sleep(1)
        with right_lock:
            print(f'step2 lock->{right_lock}')


l = threading.Lock()
r = threading.Lock()

t1 = threading.Thread(target=die_lock, args=[l, r])

t2 = threading.Thread(target=die_lock, args=[r, l])

t1.start()
t2.start()
