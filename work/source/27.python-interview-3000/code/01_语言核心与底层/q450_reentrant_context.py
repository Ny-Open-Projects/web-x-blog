import contextlib
import threading

def tag(name):
    @contextlib.contextmanager
    def ctx():
        print(f"enter {name}")
        yield
        print(f"exit {name}")
    return ctx()                          # 返回实例:只能用一次

if __name__ == "__main__":
    ctx = tag("g")
    with ctx:                             # 第一次正常
        pass
    try:
        with ctx:                         # 复用同一实例
            pass
    except (RuntimeError, AttributeError) as e:
        print("reuse rejected:", type(e).__name__, "-", e)

    lock = threading.Lock()
    got1 = lock.acquire(timeout=0.05)
    got2 = lock.acquire(timeout=0.05)     # 同线程二次 acquire:会死锁,超时演示
    print("lock reentrant:", got1, got2)
    lock.release()

    rlock = threading.RLock()
    first = rlock.acquire()
    second = rlock.acquire()              # RLock 可重入:立即成功
    print("rlock reentrant:", first, second)
    rlock.release()
    rlock.release()
