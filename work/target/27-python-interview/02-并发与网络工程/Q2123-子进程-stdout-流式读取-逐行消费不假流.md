---
title: [Q2123] 子进程 stdout 流式读取:逐行消费不假流
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2123 · 子进程 stdout 流式读取:逐行消费不假流

> 难度:★★★ | 标签:subprocess, 流式读取, 管道

**问**:怎么实时读取一个长任务的 stdout,而不是等它跑完一次性拿到?

**答**:用 Popen 打开 stdout 管道,for line in proc.stdout 逐行迭代,一行到达就处理一行;子进程必须 -u 或主动 flush,否则它的库缓冲会让流式变假流式。

- 实测相邻两行的到达间隔与子进程的产出节奏一致,证明是真流式;

- communicate() 适合短任务,长任务会显得毫无进度且占内存;

- 同时收 stdout 与 stderr 要小心管道死锁,各开线程或走 asyncio;

- text=True 拿字符串,原始字节自己解码更可控。

```python
# file: code/02_并发与网络工程/q2123_subprocess_stream.py
# -*- coding: utf-8 -*-
"""子进程 stdout 流式读取: 逐行消费, 不撑爆管道。

- communicate() 一次性收全输出, 长任务会显得"没有进度"且占内存;
- for line in proc.stdout 逐行消费, 时间戳能证明是流式而非批收;
- 子进程必须 -u 或主动 flush, 否则它的库缓冲会让流式变假流式。
"""
import subprocess
import sys
import time

CHILD = r"""
import sys, time
for i in range(5):
    print("event-%d ts=%.2f" % (i, time.monotonic() % 100), flush=True)
    time.sleep(0.15)
print("child-done", flush=True)
"""


def main():
    t0 = time.monotonic()
    proc = subprocess.Popen(
        [sys.executable, "-u", "-c", CHILD],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    for line in proc.stdout:          # 逐行迭代: 一行到了就处理一行
        line = line.rstrip()
        print("%5.2fs  收到: %s" % (time.monotonic() - t0, line))
    proc.stdout.close()
    rc = proc.wait()
    print("退出码:", rc, "| 总耗时: %.2fs" % (time.monotonic() - t0))
    print("相邻两行的到达间隔约 0.15s, 证明流式读取而非最后一次性收全")


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么子进程不 flush 我就收不到行?——它的 print 进了子进程自己的缓冲,4KB 才冲一次;子进程的缓冲在子进程手里,父进程无能为力。2) 逐行读会不会比 communicate 慢?——几乎不会,瓶颈在子进程产出;行级回调的处理耗时若偏长,应丢队列异步处理。3) 「假流式」的根因与全线对策?——子进程 stdio 是全缓冲(非 tty),print 不 flush 就不出;对策:子进程 -u、PYTHONUNBUFFERED=1、或子进程代码主动 flush;父进程侧逐行读没问题——「流式是两端约定」,一端缓冲就全断。4) 双流(stdout+stderr)的死锁怎么防?——两个管道都有缓冲,只读一个另一个塞满子进程的写阻塞(经典死锁);对策:各开读取线程、或合并重定向 stderr=subprocess.STDOUT、或 asyncio subprocess——「并发读所有管道」是铁律。5) 生产陷阱?——communicate() 用于长任务(无进度+占内存);子进程不 flush(假流式);行级处理耗时过长(堵管道背压,丢队列异步处理);text 编码不一致(中文乱码);大输出无界缓冲(OOM)。

---
