import threading

counter = 0
lock = threading.Lock()
barrier = threading.Barrier(4)


def worker(use_lock: bool, n_iter: int = 200000) -> None:
    global counter
    barrier.wait()  # 4 线程集合后同时起跑, 最大化碰撞
    for _ in range(n_iter):
        if use_lock:
            with lock:
                counter += 1
        else:
            counter += 1  # 读-改-写非原子


def stress(use_lock: bool) -> int:
    global counter
    counter = 0
    ts = [threading.Thread(target=worker, args=(use_lock,)) for _ in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return counter


if __name__ == "__main__":
    expected = 4 * 200000
    for attempt in range(3):
        got = stress(use_lock=False)
        print(f"无锁 第{attempt + 1}轮: {got} / {expected} (丢失 {expected - got})")
    got = stress(use_lock=True)
    print(f"加锁: {got} / {expected}")
    assert got == expected
