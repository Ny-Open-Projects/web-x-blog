---
title: [Q2112] daemon 线程的退出时机实测:没人等,终被斩
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2112 · daemon 线程的退出时机实测:没人等,终被斩

> 难度:★★☆ | 标签:daemon, 解释器关闭, shutdown

**问**:daemon 线程是在主线程 return 的那一瞬间被杀掉的吗?它死的时候正在写的文件会怎样?

**答**:实测的答案比教条有趣:主线程返回后解释器要先 join 全部非 daemon 线程,这段时间 daemon 还在跑,直到最终化阶段才被突然掐断。

- daemon 不是死于主线程 return,而是死于解释器关闭序列的最后一段;

- 死在哪个瞬间,输出就停在哪一行,被腰斩的写盘会留下不完整数据;

- 它没有任何机会执行 finally 之外的收尾,依赖它的落盘必须有显式 stop 流程;

- 对照组:非 daemon 线程在关闭序列开头就被 join,final-line 完整落盘。

```python
# file: code/02_并发与网络工程/q2112_daemon_exit_timing.py
# -*- coding: utf-8 -*-
"""daemon 线程的退出时机实测: 没人等它, 终被腰斩。

- 主线程返回并不会立刻杀 daemon: 解释器先 join 全部非 daemon 线程;
- 这段等待期里 daemon 还在跑, 但已经没人对它负责;
- 到最终化阶段 daemon 被直接掐断, 停在哪一行算哪一行, final-line 永远缺席。
"""
import atexit
import os
import tempfile
import threading
import time


def writer(path, rounds, interval):
    with open(path, "w") as f:
        for i in range(rounds):
            f.write("line-%d\n" % i)
            f.flush()
            time.sleep(interval)
        f.write("final-line\n")   # 收尾行: 完整跑完才会出现
        f.flush()


def count_lines(path):
    with open(path) as f:
        return len([ln for ln in f if ln.strip()])


def report(daemon_file, normal_file, rounds):
    d = count_lines(daemon_file)
    print("daemon 文件行数: %d / %d, final-line 缺失 -> 被腰斩" %
          (d, rounds + 1))
    print("normal 文件行数: %d / %d, 含 final-line -> 被解释器等完" %
          (count_lines(normal_file), rounds + 1))
    for p in (daemon_file, normal_file):
        try:
            os.remove(p)
        except OSError:
            pass


def main():
    rounds = 30
    daemon_file = tempfile.mktemp(prefix="q2112_daemon_")
    t = threading.Thread(target=writer, args=(daemon_file, rounds, 0.06),
                         name="daemonic-writer", daemon=True)
    t.start()
    time.sleep(0.25)   # daemon 先写上若干行, 主线程提前退场
    print("main 返回时刻 daemon alive:", t.is_alive())
    print("此后解释器还要先等非 daemon 线程, daemon 无人负责但仍可运行")

    normal_file = tempfile.mktemp(prefix="q2112_normal_")
    t2 = threading.Thread(target=writer, args=(normal_file, rounds, 0.005),
                          name="normal-writer")
    t2.start()
    atexit.register(report, daemon_file, normal_file, rounds)


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么 daemon 里打开的数据库连接不能指望自动提交?——最终化阶段它随时被斩,连接析构可能根本没跑,事务直接丢。2) 生产上怎么"杀"daemon 才体面?——给 daemon 一个 Event 停止标志,主流程退出前 set 并限时 join,把斩首换成握手。3) 「斩首」的具体时机与后果?——解释器最终化阶段 Py_Finalize 摘除 daemon 线程:它可能在任意字节码边界停摆,正在写的缓冲半途而废、锁未释放、finally 未执行——「daemon 里不做关键落盘」由此而来;3.12 的 threading.atexit 把收尾钩子显式化是补丁不是豁免。4) 体面下线协议怎么设计?——停止 Event→set 后 join(timeout)→超时记录并接受(或升级杀进程);关键数据的持久化移出 daemon(同步写或队列+主线程消费)——「daemon 只做可丢的工作」是设计纪律不是技巧。5) 生产陷阱?——daemon 里写文件/提交事务(数据截断);daemon 持有主线程也要用的锁(退出序列死锁);假设 daemon 会在进程退出前跑完(时序赌注);把收尾逻辑写在 daemon 的 finally 里(可能根本不执行)。

---
