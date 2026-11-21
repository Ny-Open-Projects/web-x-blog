---
title: [Q1103] 多进程日志不丢 QueueHandler
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1103 · 多进程日志不丢 QueueHandler

> 难度:★★★★ | 标签:logging, multiprocessing

**问**:8 个进程同时写日志文件,出现丢行和交叉乱写,正确方案是什么?

**答**:官方方案 QueueHandler + QueueListener:子进程只把日志记录放进 multiprocessing.Queue,唯一的主进程 listener 从队列取出并统一写文件,单点写彻底消除交叉与丢行。反模式是各进程各自 FileHandler 直接写同一文件,多缓冲交错必然乱序。工程细节:listener 要在所有子进程结束后 stop() 排空队列再退出,否则尾部日志丢失;级别过滤放子进程侧,减少 IPC 量;容器环境下更常见的替代是每进程写 stdout 由采集器聚合。

```python
# file: code/05_数据分析与工程化/q1103_queue_logging.py
import logging
import logging.handlers
import multiprocessing as mp

def worker(q, n):
    logger = logging.getLogger(f"worker{n}")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.handlers.QueueHandler(q))
    for i in range(3):
        logger.info("来自 worker %s 的第 %s 条日志", n, i)

def start_listener(q):
    logging.basicConfig(level=logging.INFO, format="[统一写出] %(message)s")
    root = logging.getLogger()
    ql = logging.handlers.QueueListener(q, root.handlers[0])
    ql.start()
    return ql

if __name__ == "__main__":
    mp.set_start_method("spawn")
    q = mp.Queue()
    ql = start_listener(q)
    ps = [mp.Process(target=worker, args=(q, i)) for i in range(2)]
    for p in ps:
        p.start()
    for p in ps:
        p.join()
    q.put(None)      # 哨兵结束 listener
    ql.stop()        # stop 会排空剩余队列,保证不丢尾日志
    print("子进程只入队,主进程单点写盘")
```

**追问**:
- 追问 1:listener 挂了会怎样?—— 队列塞满后子进程 put 阻塞,拖死业务,所以 listener 要独立线程并监控队列水位。
- 追问 2:为什么容器里倾向 stdout 直写?—— 12-factor 原则,日志是事件流,采集器 sidecar 聚合,进程内不再管文件轮转。
