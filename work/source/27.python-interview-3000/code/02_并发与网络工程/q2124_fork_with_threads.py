# -*- coding: utf-8 -*-
"""fork 与线程的组合禁忌: 子进程继承的是锁的瞬间状态。

- fork 只复制调用它的那个线程, 其他线程连同它们的栈一起消失;
- 但互斥锁是进程内存, 若 fork 瞬间别的线程正持锁, 子进程继承一把"永久锁";
- 子进程里没人能解锁, 一切等这把锁的代码全部死锁。
"""
import os
import sys
import threading
import time

lock = threading.Lock()
locked_evt = threading.Event()
release_evt = threading.Event()


def holder():
    lock.acquire()
    locked_evt.set()          # 通知主线程: 锁已被我持有, 可以 fork 了
    release_evt.wait()        # 模拟长临界区, 等 fork 实验做完
    lock.release()


def main():
    t = threading.Thread(target=holder, name="holder")
    t.start()
    locked_evt.wait()

    pid = os.fork()
    if pid == 0:
        # 子进程: 内存是拷贝, 锁处于 locked 状态, 持有者线程并不存在
        ok = lock.acquire(timeout=0.5)
        print("[child] 尝试拿锁:", "成功" if ok else "失败, 锁永久卡死",
              flush=True)
        os._exit(0 if ok else 3)

    # 父进程: 先让子进程跑完实验, 再放掉真正的持有者
    _, status = os.waitpid(pid, 0)
    code = os.waitstatus_to_exitcode(status)
    print("[parent] 子进程退出码:", code)
    if code == 3:
        print("[parent] 禁忌复现: fork 时别的线程持锁 -> 子进程死锁")
    release_evt.set()
    t.join()
    print("[parent] 父进程锁状态正常, 只有子进程继承了坏状态")

    # 正确姿势: fork 前保证没有其他线程持锁, 或改用 spawn 启动方式
    mp = __import__("multiprocessing")
    print("[parent] spawn 启动方式不继承任何线程状态, 是混合场景的安全选项",
          "| 平台默认:", mp.get_start_method())


if __name__ == "__main__":
    main()
