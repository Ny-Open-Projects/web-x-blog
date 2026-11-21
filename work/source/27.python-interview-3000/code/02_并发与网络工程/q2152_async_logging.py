# -*- coding: utf-8 -*-
"""日志的异步化: QueueHandler 与 QueueListener。

- 业务线程只往内存队列塞记录, 慢接收端由 listener 线程独占承担;
- 实测: 模拟远程 syslog 的慢 sink, 异步化把单条日志调用降到微秒级;
- 代价: 进程崩溃时队列里未刷出的日志会丢, 关键审计日志要另走同步路。
"""
import logging
import logging.handlers
import os
import queue
import tempfile
import threading
import time

q = queue.Queue(-1)


class SlowSink(logging.Handler):
    """模拟慢接收端: 远程 syslog / 审计中转, 每条要 0.3ms。"""

    def emit(self, record):
        time.sleep(0.0003)
        self.format(record)


def make_async_logger(sink, name="q2152-async"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.handlers = [logging.handlers.QueueHandler(q)]
    listener = logging.handlers.QueueListener(q, sink)
    listener.start()
    return logger, listener


def make_sync_logger(sink, name="q2152-sync"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    logger.handlers = [sink]
    return logger


def bench(logger, n=200, threads=1):
    def worker(k):
        for i in range(n):
            logger.info("event-%d payload=%s", k * n + i, "x" * 64)
    ts = [threading.Thread(target=worker, args=(k,)) for k in range(threads)]
    t0 = time.monotonic()
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    return (time.monotonic() - t0) / (n * threads)


def main():
    sink = SlowSink()

    logger, listener = make_async_logger(sink)
    async_us = bench(logger, n=200, threads=3) * 1e6
    listener.stop()                       # 排干队列并停 listener
    print("异步化: 3 业务线程单条 %.1f us (只入队, 慢 IO 在 listener 线程)" %
          async_us)

    logger2 = make_sync_logger(sink, name="q2152-sync-2")
    sync_us = bench(logger2, n=200, threads=3) * 1e6
    print("同步写: 3 业务线程单条 %.1f us (每条都在等慢接收端)" % sync_us)
    print("提速约 %.0f 倍: 调用方与慢 sink 彻底解耦, 日志不再拖业务" %
          (sync_us / max(async_us, 1e-6)))

    path = tempfile.mktemp(prefix="q2152_file_")
    fh = logging.FileHandler(path)
    logger3, listener3 = make_async_logger(fh, name="q2152-file")
    bench(logger3, n=100, threads=1)
    listener3.stop()
    with open(path) as f:
        lines = sum(1 for _ in f)
    print("落盘核对: %d/100 行完整, listener.stop 保证退出前排干" % lines)
    os.remove(path)
    print("注意: 崩溃时队列内未刷出的记录会丢, 审计日志不要走异步")


if __name__ == "__main__":
    main()
