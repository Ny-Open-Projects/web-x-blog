import os
import signal
import threading
import time

received = []

def handler(signum, frame):
    received.append(signum)

if __name__ == "__main__":
    old = signal.signal(signal.SIGUSR1, handler)

    worker = threading.Thread(target=lambda: time.sleep(0.1))
    worker.start()
    worker.join()
    os.kill(os.getpid(), signal.SIGUSR1)   # 发给进程:由主线程执行 handler
    time.sleep(0.2)                        # 主线程跑字节码,处理函数才有机会运行
    print("handler saw:", received)
    signal.signal(signal.SIGUSR1, old)

    def try_register():
        try:
            signal.signal(signal.SIGUSR1, handler)
        except ValueError as e:
            print("worker thread:", e)

    t = threading.Thread(target=try_register)
    t.start()
    t.join()
