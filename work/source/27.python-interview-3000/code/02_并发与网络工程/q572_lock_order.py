import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()
lock_a_id, lock_b_id = id(lock_a), id(lock_b)  # 固定全局顺序的依据


def transfer_ordered(amount: float) -> None:
    """手段一: 永远先拿 id 较小的锁。"""
    first, second = (lock_a, lock_b) if lock_a_id < lock_b_id else (lock_b, lock_a)
    with first:
        time.sleep(0.05)
        with second:
            pass  # 临界区: 转账


def transfer_fallback(amount: float) -> bool:
    """手段二: try-acquire 失败则回退重来, 破坏持有并等待。"""
    while True:
        if lock_a.acquire(timeout=0.05):
            try:
                if lock_b.acquire(timeout=0.05):
                    try:
                        return True
                    finally:
                        lock_b.release()
            finally:
                lock_a.release()
        time.sleep(0.01)  # 退避, 防活锁加剧


if __name__ == "__main__":
    # 反例: 固定顺序 vs 乱序 — 乱序版本会死锁, 这里用超时探测证明
    def t_bad_1() -> None:
        with lock_a:
            time.sleep(0.1)
            got = lock_b.acquire(timeout=0.3)
            if not got:
                print("bad_1: 拿 lock_b 超时 → 若无超时这里就是死锁")
            else:
                lock_b.release()

    def t_bad_2() -> None:
        with lock_b:
            time.sleep(0.1)
            got = lock_a.acquire(timeout=0.3)
            if not got:
                print("bad_2: 拿 lock_a 超时 → 构成循环等待")
            else:
                lock_a.release()

    t1 = threading.Thread(target=t_bad_1)
    t2 = threading.Thread(target=t_bad_2)
    t1.start(); t2.start()
    t1.join(); t2.join()

    ts = [threading.Thread(target=transfer_ordered, args=(1,)) for _ in range(4)]
    ts += [threading.Thread(target=transfer_fallback, args=(1,)) for _ in range(4)]
    t0 = time.perf_counter()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print(f"排序+回退版本 8 个任务全部完成, 耗时 {time.perf_counter() - t0:.2f}s")
