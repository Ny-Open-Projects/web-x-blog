---
title: [Q2114] threading.excepthook:线程异常的默认打印与钩子
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2114 · threading.excepthook:线程异常的默认打印与钩子

> 难度:★★★ | 标签:excepthook, 线程异常, 崩溃埋点

**问**:线程里抛了异常,主线程没 join 到任何报错,这个异常去哪了?怎么把它接住?

**答**:3.8 起线程异常默认交给 threading.excepthook,打印"Exception in thread 名字"加栈到 stderr 后线程终止、进程继续,默认行为可以被整只替换。

- ExceptHookArgs 携带 exc_type、exc_value、exc_traceback 与 thread;

- 默认打印包含线程名,是定位崩线程的首要线索;

- 自定义钩子把打印换成结构化上报,生效期间 stderr 不再有散装栈;

- 钩子必须自己兜底:钩子内部再抛异常,解释器只能再次打印并继续。

```python
# file: code/02_并发与网络工程/q2114_excepthook_default.py
# -*- coding: utf-8 -*-
"""threading.excepthook: 线程异常的默认行为与自定义钩子。

- 3.8 起线程异常不再杀进程, 默认由 threading.excepthook 打印到 stderr 后继续跑;
- ExceptHookArgs 携带 exc_type / exc_value / exc_traceback / thread;
- 自定义钩子把默认打印替换掉, 是崩溃埋点的唯一正门。
"""
import io
import threading
import contextlib


def boom(name):
    raise ValueError("worker %s 崩了" % name)


def default_behavior():
    buf = io.StringIO()
    t = threading.Thread(target=boom, args=("A",), name="t-A")
    with contextlib.redirect_stderr(buf):   # 捕获默认钩子的打印
        t.start()                            # 必须在捕获内启动, 否则竞态漏拍
        t.join()
    out = buf.getvalue()
    print("默认钩子打印包含异常类型:", "ValueError" in out)
    print("默认钩子打印包含线程名:", "t-A" in out)
    print("进程此刻仍然存活, 这行就是证明")


caught = []


def custom_hook(args):
    caught.append({
        "thread": args.thread.name,
        "type": args.exc_type.__name__,
        "msg": str(args.exc_value),
    })


def main():
    default_behavior()

    old = threading.excepthook
    threading.excepthook = custom_hook
    try:
        t = threading.Thread(target=boom, args=("B",), name="t-B")
        t.start()
        t.join()
    finally:
        threading.excepthook = old   # 用完恢复, 避免污染其他库
    print("自定义钩子捕获:", caught)
    print("自定义钩子生效期间默认 stderr 打印消失, 改为结构化上报")


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么线程异常不像主线程那样让进程退出?——线程边界就是隔离边界,一个后台线程崩掉不应拖垮整个进程,代价是异常容易被无视,所以要配钩子。2) 线程池里的异常也走 excepthook 吗?——submit 的异常存在 Future 里由 result 抛出,不走 excepthook;只有 fire-and-forget 的裸线程才依赖它。3) excepthook 与线程池 Future 的分工边界?——裸 Thread 的异常走 excepthook(无人 join 的出口);ThreadPoolExecutor.submit 的异常存在 Future 里由 result() 抛出,不走钩子——「fire-and-forget 的裸线程才依赖它」;混合使用时要分别管收尾(Q1587 的任务收尾纪律)。4) ExceptHookArgs 里有什么可挖的?——exc_type/value/traceback+thread(线程名定位);自定义钩子把打印换成 JSONL 上报(Q2115 工程化);钩子自身必须全兜底(钩子再抛解释器只能再打印)。5) 生产陷阱?——替换钩子后忘记链式调用原钩子(默认日志丢失);钩子里做阻塞上报(放大事故,先落盘异步上报,Q2115);以为「线程崩了进程会退」(不会,异常被吞成 stderr 一行);测试期替换钩子不恢复(污染其他库)。

---
