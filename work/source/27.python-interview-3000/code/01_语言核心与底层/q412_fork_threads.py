import os
import sys
import threading
import time

lock = threading.Lock()

def locker():
    while True:
        with lock:            # 后台线程反复短暂持锁
            time.sleep(0.001)

threading.Thread(target=locker, daemon=True).start()
time.sleep(0.05)              # 大概率 fork 时锁恰被后台线程持有

pid = os.fork()               # 仅当前线程被复制,锁状态被复制
if pid == 0:
    # 子进程:尝试获取一把可能"已死"的锁 —— 竞争窗口内会永久阻塞
    got = lock.acquire(timeout=1)
    print("child acquired:", got)
    os._exit(0)
else:
    _, status = os.waitpid(pid, 0)
    print("child exit status:", status)
    print("start methods available:", __import__("multiprocessing").get_all_start_methods())
