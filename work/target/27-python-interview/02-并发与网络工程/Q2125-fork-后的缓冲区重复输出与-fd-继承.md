---
title: [Q2125] fork 后的缓冲区重复输出与 fd 继承
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2125 · fork 后的缓冲区重复输出与 fd 继承

> 难度:★★★ | 标签:fork, stdio 缓冲, fd

**问**:fork 出来的子进程打印日志,为什么日志文件里出现重复内容?

**答**:fork 复制整份用户态内存,包括未 flush 的 stdio 缓冲;父子各自 flush 同一段缓冲,内容就写两遍。

- 实验文件里 parent-before 出现两次:子进程的缓冲拷贝里也有一份;

- 已打开的 fd 在父子间共享同一文件偏移,追加写不会互相覆盖;

- 修复是 fork 前 flush,或子进程立刻重开文件;

- 终端上行缓冲让它难以复现,重定向到文件才现形。

```python
# file: code/02_并发与网络工程/q2125_fork_buffer_fd.py
# -*- coding: utf-8 -*-
"""fork 后的缓冲区重复输出与 fd 继承。

- fork 复制整份用户态内存, 未 flush 的 stdio 缓冲也被复制;
- 父子各自 flush 同一段缓冲, 内容就会写两遍;
- 已打开的 fd 在父子间共享同一个文件偏移, 追加写不会互相覆盖。
"""
import os
import tempfile

path = tempfile.mktemp(prefix="q2125_forkbuf_")


def main():
    f = open(path, "w", buffering=8192)   # 文件默认全缓冲, 终端才是行缓冲
    f.write("parent-before\n")            # 先写不 flush: 驻留父进程缓冲

    pid = os.fork()
    if pid == 0:
        # 子进程拿到缓冲的完整拷贝, 其中也有 parent-before
        f.write("child\n")
        f.flush()                         # 子进程冲出: parent-before + child
        os._exit(0)

    os.waitpid(pid, 0)
    f.write("parent-after\n")
    f.flush()                             # 父进程又冲出一份 parent-before
    f.close()

    with open(path) as rf:
        content = rf.read()
    print("文件内容:", repr(content))
    dup = content.count("parent-before")
    print("parent-before 出现次数:", dup, "-> 缓冲被 fork 复制后各自 flush")

    # 修复: fork 前 flush, 或者 fork 后子进程立刻重开文件
    f2 = open(path, "w")
    f2.write("clean-parent\n")
    f2.flush()                            # 关键: fork 前冲掉
    pid2 = os.fork()
    if pid2 == 0:
        f2.write("clean-child\n")
        f2.flush()
        os._exit(0)
    os.waitpid(pid2, 0)
    f2.write("clean-after\n")
    f2.flush()
    f2.close()
    with open(path) as rf:
        print("flush 后内容:", repr(rf.read()))
    os.remove(path)


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么终端上看不到这个问题?——tty 是行缓冲,每次 print 都已 flush,没有残留缓冲可复制。2) sendfile/write 这类系统调用有这个问题吗?——没有,缓冲只在用户态 stdio 层,直接 write 的数据不经过它。3) 缓冲重复的完整机制链?——fork 复制用户态内存(含 stdio 缓冲内容)→父子各自缓冲里都有同一份未 flush 数据→各自 flush 时写两遍;fd 共享文件偏移所以追加不覆盖——「重复+不覆盖」的组合让日志双份;对策 fork 前 flush 或子进程重开文件。4) 与 Q2124 的死锁问题怎么一起防?——「fork 只做 exec」同时解决缓冲与锁两类继承问题;不能 exec 时(纯 Python fork)要在 fork 前:flush 一切、停线程、清理锁持有——清单化执行。5) 生产陷阱?——日志重复被误当「重复上报 bug」排查半天;重定向到文件才复现(tty 行缓冲掩盖);子进程里 print 不 flush(Q2123 同源);fd 继承泄漏(close_fds=False 留下不该有的 fd);缓冲方案换 sys.stdout.reconfigure(line_buffering=True) 误以为解决 fork 重复(不解决,复制的还是已缓冲内容)。

---
