---
title: "[Q5706] os.exec：进程替换发生时 fd 去留的裁决规则"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5706 · os.exec：进程替换发生时 fd 去留的裁决规则

难度：P6 ｜ 标签：os.exec、execv、CLOEXEC、set_inheritable、fork、fd 泄漏

**问**：`os.fork` 后调用 `os.execv` 替换成新程序，原来打开的 socket/pipe 文件描述符还在吗？为什么有时新程序能拿到父进程的 fd，有时拿不到？`O_CLOEXEC` / `set_inheritable(False)` 到底在哪个时刻起作用？这个规则为什么能防止 fd 泄漏？

**答**：
结论：fork 阶段**无条件复制**全部 fd（子进程与父进程共享同一文件表项）；exec 阶段按**每个 fd 的 close-on-exec 标志**裁决——标志置位的 fd 在 exec 成功瞬间自动关闭，未置位的存活下来编号不变。Python 3.4 起 PEP 446 把默认值反转为"不可继承"：`socket`/`os.pipe` 创建的 fd 默认 `set_inheritable(False)`，即默认 CLOEXEC 生效，这是为了堵"子进程意外继承监听 socket/日志文件"的泄漏口子。想让子进程拿到 fd，必须显式 `set_inheritable(True)`（或 `subprocess` 的 `pass_fds`）。判断"fork 与 exec 谁决定 fd 去留"是面试的经典陷阱：fork 全继承，exec 才过滤。

取舍：a) 默认 CLOEXEC 是安全侧的默认值：exec 后"恰好还在"的 fd 更可能是 bug 而非设计，子进程持有的无关 fd 会锁住文件、占住端口、绕过权限模型；b) 需要跨 exec 传递 fd 的正当场景（热升级交接监听 socket、pipe 通道）必须显式声明可继承，让代码里的"意外传递"变成"审查过的传递"；c) `os.open` 支持 `O_CLOEXEC` 原子设置，避免"open 后 set_inheritable 前被并发线程 fork"的窗口；d) 演示/排查时可在子进程里 `os.listdir('/dev/fd')` 或对可疑 fd `fstat` 看它是否存活；e) 多线程服务里更推荐 `subprocess(close_fds=True)`（默认）+ `pass_fds` 白名单，而不是手写 fork+exec。

实战：事故形态是"配置热重载进程 fork 出校验子进程，子进程意外继承了主服务的监听 socket（旧版代码 set_inheritable(True) 又没撤销），重启主服务时端口始终占用，日志只有一行 Address already in use；排查 lsof 发现子进程持着 0.0.0.0:8080"。下面演示 CLOEXEC 裁决：fork 后 exec，看 fd 的去留。

```python
import os
import sys

CHECK = (
    "import sys, os\n"
    "fd = int(sys.argv[1])\n"
    "out = int(sys.argv[2])\n"
    "try:\n"
    "    os.fstat(fd)\n"
    "    verdict = 'fd 在 exec 后存活（可继承）'\n"
    "except OSError:\n"
    "    verdict = 'fd 已被 exec 关闭（CLOEXEC 生效）'\n"
    "os.write(out, verdict.encode())\n"
)


def spawn(inheritable):
    r, w = os.pipe()                       # 被检查的 fd
    or_, ow = os.pipe()                    # 回传结论的管道
    os.set_inheritable(w, inheritable)
    os.set_inheritable(ow, True)
    pid = os.fork()
    if pid == 0:
        os.close(r)
        os.close(or_)
        os.execv(sys.executable,
                 [sys.executable, "-c", CHECK, str(w), str(ow)])
    os.close(w)
    os.close(ow)
    out = os.read(or_, 4096).decode()
    os.waitpid(pid, 0)
    os.close(r)
    os.close(or_)
    return out.strip()


print("[1] set_inheritable(False):", spawn(False))
print("[2] set_inheritable(True) :", spawn(True))
print("[3] fork 复制 fd，exec 按 CLOEXEC 位裁决去留——fork 与 exec 的 fd 语义分两步")
```

**追问一**：为什么 `O_CLOEXEC` 强调"原子设置"而 `set_inheritable` 不行？—— `set_inheritable` 是 open 之后单独一次调用，两步之间如果另一个线程执行 fork+exec，新 fd 还带着可继承标志就 exec 了，fd 泄漏窗口出现。`os.open(..., O_CLOEXEC)` 把"打开"与"标记"合成一条系统调用，没有中间态。Python 标准库自身（socket、pipe）在创建时即设 CLOEXEC，就是为了消除这个窗口；应用层要跨 exec 传 fd 时才显式翻转。

**追问二**：`subprocess` 的 `close_fds=True` 和 `pass_fds` 与这套规则什么关系？—— `close_fds=True`（3.2+ 默认）表示 exec 目标程序里除标准流（0/1/2）和 `pass_fds` 指定的 fd 外全部关闭，实现上是 subprocess 在 exec 前替你把所有无关 fd 设 CLOEXEC（现代实现用 `close_range` 一次完成）。`pass_fds` 白名单里的 fd 会被自动置为可继承。所以绝大多数场景不需要手写 fork+exec：`Popen(..., pass_fds=(w,))` 一行表达"只传这一个 fd"，同时天然继承默认防泄漏语义。

## 背诵要点
- fork 无条件复制全部 fd；exec 按 CLOEXEC 位裁决去留——去留是 exec 决定的，不是 fork。
- Python 3.4+（PEP 446）fd 默认不可继承；跨 exec 传 fd 必须显式 `set_inheritable(True)` 或 `pass_fds`。
- `O_CLOEXEC` 原子设置消除"open 后被并发 fork"的泄漏窗口；排查用 `/dev/fd` 或 fstat 验证存活。

## 复盘追问
- 重启时报 Address already in use，lsof 发现旧子进程占着端口，根因是什么？（子进程 exec 后继承了监听 socket，CLOEXEC 未置位）
- subprocess 默认为什么不会再有 fd 泄漏？（close_fds=True 默认 + pass_fds 白名单 + 库内 CLOEXEC）
