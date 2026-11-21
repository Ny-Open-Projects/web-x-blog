import threading

rlock = threading.RLock()


def inner() -> None:
    with rlock:  # 同一线程再次进入, RLock 允许
        print("inner 拿到锁")


def outer() -> None:
    with rlock:
        print("outer 拿到锁")
        inner()
        print("outer 释放前 depth 正确")


if __name__ == "__main__":
    outer()

    plain = threading.Lock()
    got = plain.acquire()
    result = {}
    def try_reacquire() -> None:
        result["got"] = plain.acquire(timeout=0.1)
    t = threading.Thread(target=try_reacquire)
    t.start()
    t.join()
    print("Lock 同线程再次 acquire 是否成功:", bool(result.get("got")), "(False 表示死锁被超时解除)")
    plain.release()
