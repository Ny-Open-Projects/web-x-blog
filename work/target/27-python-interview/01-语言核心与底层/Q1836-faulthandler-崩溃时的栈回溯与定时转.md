---
title: [Q1836] faulthandler:崩溃时的栈回溯与定时转储
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1836 · faulthandler:崩溃时的栈回溯与定时转储

> 难度:★★☆☆☆ | 标签:faulthandler, 崩溃诊断, 运维

**问**:进程段错误直接死掉什么都不留,怎么让 CPython 在崩溃瞬间吐出 Python 栈?

**答**:faulthandler.enable() 挂上 SIGSEGV/SIGFPE/SIGABRT 等致命信号的处理器,崩溃时把所有线程的 Python 级栈写到指定文件(通常 sys.stderr)——纯 C 栈对 Python 工程师没用,这一层翻译是它的价值。两个主动工具:① dump_traceback(file) 手动转储当前所有线程栈,是线上「进程卡住」时 py-spy 之前的最小手段;② dump_traceback_later(timeout, file, exit=False) 起看门狗线程,超时自动转储,cancel_dump_traceback_later 撤销,demo 里 0.05 秒后成功转储且进程活着。生产姿势:入口处 enable(file=sys.stderr) 是无代价保险;定时转储适合「怀疑某段循环卡死」的现场取证,与 Q1561 的 excepthook 互补——一个管未捕获异常,一个管解释器级崩溃。

```python
# file: code/01_语言核心与底层/q1836_faulthandler.py
"""faulthandler:崩溃时的栈回溯与定时转储。"""
import faulthandler
import sys
import tempfile
import time


def dump_all_threads():
    with tempfile.TemporaryFile(mode="w+") as tf:
        faulthandler.dump_traceback(file=tf)   # 手动转储所有线程的 Python 栈
        tf.seek(0)
        return tf.read()


def timed_dump():
    with tempfile.TemporaryFile(mode="w+") as tf:
        faulthandler.dump_traceback_later(0.05, file=tf, exit=False)
        time.sleep(0.12)                       # 让定时器到期,把栈写进文件
        faulthandler.cancel_dump_traceback_later()
        tf.seek(0)
        return tf.read()


if __name__ == "__main__":
    faulthandler.enable(file=sys.stderr)       # 生产入口的标准动作
    print("enable 后 is_enabled:", faulthandler.is_enabled())
    text = dump_all_threads()
    print("手动转储捕获到本文件:", "q1836_faulthandler.py" in text)
    print("定时转储捕获到本文件:", "q1836_faulthandler.py" in timed_dump())
    faulthandler.disable()
    print("disable 后 is_enabled:", faulthandler.is_enabled())
```

**追问**:1) faulthandler 的转储信号安全吗?——处理器只调用 async-signal-safe 的 write,不分配内存不做 Python 调用,所以崩溃路径上仍然可靠;这也是它打不出丰富信息的原因。2) 三种触发方式?——崩溃信号(SIGSEGV/SIGFPE/SIGABRT 等)自动转储、faulthandler.dump_traceback_later 定时看门狗、register 注册自定义信号;全部只打印「哪个线程哪一行」。3) 与调试器的分工?——faulthandler 管「崩溃时留证据」(生产),GDB/lldb 管「现场深挖」(开发);核心转储配合 coredumpctl。4) 生产陷阱?——未启用 faulthandler,崩溃只剩 exit code;采集管道忽略 stderr 丢转储;定时转储的文件句柄没关。
