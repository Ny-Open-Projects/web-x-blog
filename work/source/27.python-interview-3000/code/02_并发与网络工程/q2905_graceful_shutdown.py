# -*- coding: utf-8 -*-
"""优雅停机的标准范式: 信号 -> 停收 -> 排空 -> 收尾 -> 退出码。

- 信号处理器只做一件事: 置停止位 (信号处理器里不干重活);
- 工作线程把在途任务做完, 排空有 deadline, 超时就有强杀预案;
- 收尾落盘 + 用退出码告诉编排层: 这次关得干不干净。
"""
import os
import queue
import signal
import threading
import time

stop = threading.Event()
results = []
rlock = threading.Lock()


def worker(q, wid):
    """工作线程: 停止位只挡新任务, 在途任务必须做完。"""
    while True:
        try:
            item = q.get(timeout=0.05)
        except queue.Empty:
            if stop.is_set():
                break                   # 停机且没活了, 收工
            continue
        try:
            time.sleep(0.01)            # 模拟在途任务的处理耗时
            with rlock:
                results.append(item * item)
        finally:
            q.task_done()


def main():
    q = queue.Queue()
    ws = [threading.Thread(target=worker, args=(q, i), daemon=True)
          for i in range(3)]
    for t in ws:
        t.start()

    received = []

    def on_signal(signum, frame):
        received.append(signum)         # 信号处理器: 只置位, 不干活
        stop.set()

    signal.signal(signal.SIGTERM, on_signal)
    signal.signal(signal.SIGINT, on_signal)

    for i in range(30):                 # 正常业务投递
        q.put(i)
    time.sleep(0.06)                    # 让一部分先跑起来
    os.kill(os.getpid(), signal.SIGTERM)   # 模拟外部发来停机信号
    time.sleep(0.05)

    # 范式第二步: 排空在途, 带 deadline
    deadline = time.monotonic() + 5.0
    while q.unfinished_tasks > 0 and time.monotonic() < deadline:
        time.sleep(0.01)
    drained = q.unfinished_tasks == 0
    # 范式第三步: 等工作线程退出 (超时则有强杀预案, 这里不触发)
    for t in ws:
        t.join(timeout=3)
    clean_exit = drained and not any(t.is_alive() for t in ws)

    print("收到信号: %s" % [int(s) for s in received])
    print("在途排空: %s, 工作线程全部退出: %s" % (drained, clean_exit))
    print("成果落盘 %d/%d 项" % (len(results), 30))
    exit_code = 0 if clean_exit and len(results) == 30 else 1
    print("退出码: %d (0=干净停机, 非 0=需要编排层善后)" % exit_code)
    assert received == [signal.SIGTERM]
    assert clean_exit and len(results) == 30 and exit_code == 0
    # 现实中的第二刀: deadline 到了还没排空 -> 再次收到信号直接 os._exit
    print("要点: 处理器只置位, 排空带 deadline, 结果用退出码交代")


if __name__ == "__main__":
    main()
