import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def thread_a() -> None:
    with lock1:
        time.sleep(0.1)  # 制造交错窗口
        got = lock2.acquire(timeout=0.5)
        print("thread_a 获取 lock2:", bool(got))


def thread_b() -> None:
    with lock2:
        time.sleep(0.1)
        got = lock1.acquire(timeout=0.5)
        print("thread_b 获取 lock1:", bool(got))


if __name__ == "__main__":
    a = threading.Thread(target=thread_a)
    b = threading.Thread(target=thread_b)
    a.start()
    b.start()
    a.join()
    b.join()
    # 用 timeout 后不会永久卡死, 两个 acquire 都会失败; 去掉 timeout 则真死锁
