---
title: [Q2911] 后台任务的守护化:daemon 三件套缺一丢账
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2911 · 后台任务的守护化:daemon 三件套缺一丢账

> 难度:★★ | 标签:daemon, 后台任务, 优雅停机

**问**:把定时统计、缓存刷新这类活儿丢给后台线程,daemon=True 一设就完事了吗?

**答**:没有。daemon 标志只解决"不拖住进程退出",副作用是线程随时可能被斩——账本在内存里攒着,进程一退全丢。完整的守护化是三件套:daemon 标志让进程可退出,停止位 stop 让主流程能主动通知收工,收尾钩子 flush 在 join 之后把攒的账落盘。实测对照组:规范 shutdown 的 worker,counter 与 flushed 相等,账本收平;裸奔退出的 worker,flushed 还是 0,counter 上的每一笔都要丢。还要理解 daemon 的边界:非守护线程会让解释器等它跑完,daemon 线程不会——所以"关键收尾"永远不能只交给 daemon 线程,主流程必须显式 join 加 flush。

- daemon 线程适合"丢了也不致命"的活,任何有状态的活都要有 flush;

- stop 检查的周期决定停机响应速度,处理间隔太长收工就慢;

- flush 要幂等:被调两次不能把账算两遍。

```python
# file: code/02_并发与网络工程/q2911_daemon_worker.py
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
```

**追问**:1) 进程被 SIGKILL 怎么办?——三件套全失效,这正是周期性把账小步落盘或写 WAL 的理由,daemon 化只防优雅退出时的丢账。2) daemon 线程在解释器退出时被怎么处理?——Python 不等待它们,在任意字节码边界直接终结,不存在"跑完最后一段"的保证。3) 底层机制:解释器退出时 daemon 线程死在哪一步?——threading._shutdown 只 join 非守护线程,守护线程在解释器 finalization 阶段被直接终止,锁、半写文件、半提交事务都可能留下;所以有状态的后台活必须自己保证 flush 幂等且由主流程显式驱动。4) 生产陷阱?——daemon 线程里装 signal handler 不生效(信号只在主线程处理);flush 不幂等,重复调用账翻倍;stop 检查间隔太长,停机等待超出编排层宽限被强杀。

---
