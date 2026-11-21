import faulthandler
import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()


def t1() -> None:
    with lock_a:
        time.sleep(0.2)      # 给 t2 时间拿到 lock_b
        with lock_b:         # 死锁点
            print("t1 不可能到这里")


def t2() -> None:
    with lock_b:
        time.sleep(0.2)
        with lock_a:
            print("t2 不可能到这里")


if __name__ == "__main__":
    faulthandler.enable()
    a = threading.Thread(target=t1, name="T1")
    b = threading.Thread(target=t2, name="T2")
    a.start()
    b.start()
    time.sleep(1.0)  # 此刻两个线程已互相卡死
    print("=== 模拟 kill -USR1: dump 所有线程栈 ===")
    with open("/tmp/q571_dump.txt", "w") as f:
        faulthandler.dump_traceback(file=f, all_threads=True)
    print(open("/tmp/q571_dump.txt").read())
    print("栈里能看到 T1 停在 lock_b.acquire, T2 停在 lock_a.acquire")
    import os
    os._exit(0)  # 演示结束, 真实场景这一步由运维强制重启替代
