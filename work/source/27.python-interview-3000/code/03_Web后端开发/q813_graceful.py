import os
import signal
import threading
import time

shutting_down = False
inflight = 0

def on_term(signum, frame):
    global shutting_down
    shutting_down = True                      # 1. 不再接新请求
    while inflight > 0:                       # 2. 排空在途请求
        time.sleep(0.005)
    print("3. 释放连接池与后台任务后退出")

signal.signal(signal.SIGTERM, on_term)

def handle():
    global inflight
    inflight += 1
    time.sleep(0.05)
    inflight -= 1

t = threading.Thread(target=handle)
t.start()
t.join()
os.kill(os.getpid(), signal.SIGTERM)          # 模拟编排系统发信号
time.sleep(0.1)
