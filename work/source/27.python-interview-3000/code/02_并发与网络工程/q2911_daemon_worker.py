# -*- coding: utf-8 -*-
"""后台任务的守护化: daemon 线程 + 停止位 + 退出前收尾。

- daemon=True: 后台线程不阻止进程退出, 但代价是随时可能被斩;
- 所以守护化三件套: 停止位 stop + 周期性检查停止位 + 退出前 flush;
- 对照实验: 正常 shutdown 时账本收平; 裸奔退出时最后一笔必丢。
"""
import threading
import time


class BackgroundWorker:
    """周期性后台任务: 攒账, 收到停止位后落盘。"""

    def __init__(self, name, interval=0.03):
        self.name = name
        self.interval = interval
        self.stop = threading.Event()
        self.counter = 0
        self.flushed = 0
        self.thread = threading.Thread(target=self._run, daemon=True)

    def _run(self):
        while not self.stop.is_set():
            time.sleep(self.interval)
            self.counter += 1          # 攒账: 模拟未落盘的内存态

    def start(self):
        self.thread.start()

    def flush(self):
        self.flushed = self.counter    # 收尾: 把账落盘

    def shutdown(self):
        self.stop.set()
        self.thread.join(timeout=2)
        self.flush()


if __name__ == "__main__":
    # 正确姿势: 干完活 -> stop -> join -> flush, 账本收平
    good = BackgroundWorker("good")
    good.start()
    time.sleep(0.2)                    # 主线程做业务
    good.shutdown()
    print("规范停机: counter=%d flushed=%d 收平=%s"
          % (good.counter, good.flushed, good.counter == good.flushed))
    assert good.counter == good.flushed

    # 错误姿势: 忘了 stop, 进程退出时 daemon 线程被直接斩杀
    bad = BackgroundWorker("bad")
    bad.start()
    time.sleep(0.2)
    # 假如此刻进程直接退出, bad 线程不会有任何机会 flush:
    lost = bad.counter - bad.flushed
    print("裸奔退出: counter=%d flushed=%d 将丢失 %d 笔账"
          % (bad.counter, bad.flushed, lost))
    assert lost > 0
    bad.stop.set()                     # 演示脚本仍要自己收尾
    bad.thread.join(timeout=2)
    bad.flush()

    # daemon 的边界: 守护线程不阻塞解释器退出, 反之非守护线程会拖住进程
    non_daemon_done = []
    t = threading.Thread(target=lambda: (time.sleep(0.15),
                                         non_daemon_done.append(1)))
    t.daemon = False                   # 非守护: 解释器等它
    t.start()
    t.join(timeout=2)
    print("非守护线程收尾后进程才退: done=%s" % non_daemon_done)
    assert non_daemon_done == [1]
    print("要点: 守护化 = daemon 标志 + 停止位 + 收尾钩子, 三者缺一就会丢账")
