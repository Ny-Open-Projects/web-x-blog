---
title: [Q550] import 锁与线程下的导入死锁
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q550 · import 锁与线程下的导入死锁

> 难度:★★★★★ | 标签:import, 线程

**问**:多线程同时首次 import 同一模块会怎样?什么场景会真的死锁?

**答**:导入系统有全局的模块锁机制:线程 A 首次 import m 时持锁执行 m 的顶层代码,线程 B import m 阻塞等待,最终共享同一次执行结果——所以「重复执行」不会发生,sys.modules 注册前就加锁。死锁场景:模块顶层代码里启动线程并等它 import 另一个模块,或两个线程以相反顺序交叉首次导入互相依赖的模块循环——持锁链交叉即死锁。3.3 后改为每模块锁 + 死锁检测(部分场景回退),但规范不变:import 只出现在模块顶层与函数开头,不在 import 路径中启动线程/做重活。

```python
# file: code/01_语言核心与底层/q550_import_lock.py
import sys
import threading

results = {}

def importer(name):
    try:
        __import__(name)
        results[name] = "imported"
    except ImportError as e:
        results[name] = f"ImportError: {e}"

if __name__ == "__main__":
    threads = [threading.Thread(target=importer, args=("json",)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(results)                       # 并发首次导入:只有一次真正执行
    print("single module object:", sys.modules["json"] is __import__("json"))
    print("rule: never spawn-and-join threads at module import time")
```

**追问**:1) import 锁死锁的典型线上形态?——插件系统在 import 时初始化连接池,池内工作线程又 import 配置模块,主线程持配置模块锁等池初始化完成,形成 A→B→A 环;解法是把重初始化挪到「首次使用」而非 import 期。2) per-module 锁的机制?——3.3+ 每个模块名一把锁:多线程同时导入同一模块时只有一个执行初始化,其他等锁;跨线程的循环导入仍可能死锁,规范上「import 期不做阻塞工作」。3) 与 fork 的交互?——导入锁在 fork 时可能被子进程继承成「已锁」状态,子进程 import 卡死;多线程 + fork 的组合要保证 fork 时不持导入锁(或改 spawn)。4) 生产陷阱?——import 期建连接、起线程、读远程配置;后台线程在主线程导入链里再 import;插件框架在 __init__.py 做重活。
