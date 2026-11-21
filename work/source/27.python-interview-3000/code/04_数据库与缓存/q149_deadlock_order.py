"""线程锁模拟死锁: 乱序加锁会互相等待, 统一顺序即可避免"""
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def transfer_bad(name: str, first, second, timeout: float = 0.3) -> None:
    """先抢 first 再抢 second, 两线程顺序相反就可能死锁"""
    got_first = first.acquire(timeout=timeout)
    if not got_first:
        print(name, "第一阶段等待超时退出")
        return
    got_second = second.acquire(timeout=timeout)
    if not got_second:
        first.release()
        print(name, "第二阶段等待超时, 释放已持有锁避免死锁")
        return
    try:
        print(name, "同时持有两把锁, 执行业务")
    finally:
        second.release()
        first.release()


def transfer_safe(name: str, wanted: list, timeout: float = 0.3) -> None:
    """按全局固定顺序(如按锁 id 排序)加锁, 不会循环等待"""
    ordered = sorted(wanted, key=id)
    for lk in ordered:
        if not lk.acquire(timeout=timeout):
            for held in ordered[:ordered.index(lk)]:
                held.release()
            print(name, "获取失败, 按序回退")
            return
    try:
        print(name, "安全地同时持有两把锁")
    finally:
        for lk in reversed(ordered):
            lk.release()


if __name__ == "__main__":
    print("--- 乱序 + 超时防护 ---")
    t1 = threading.Thread(target=transfer_bad, args=("T1", lock_a, lock_b))
    t2 = threading.Thread(target=transfer_bad, args=("T2", lock_b, lock_a))
    t1.start(); t2.start(); t1.join(); t2.join()

    print("--- 固定顺序 ---")
    t1 = threading.Thread(target=transfer_safe, args=("T1", [lock_a, lock_b]))
    t2 = threading.Thread(target=transfer_safe, args=("T2", [lock_b, lock_a]))
    t1.start(); t2.start(); t1.join(); t2.join()
