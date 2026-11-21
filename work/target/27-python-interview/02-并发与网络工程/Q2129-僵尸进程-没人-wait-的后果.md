---
title: [Q2129] 僵尸进程:没人 wait 的后果
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2129 · 僵尸进程:没人 wait 的后果

> 难度:★★☆ | 标签:僵尸进程, waitpid, 进程表

**问**:子进程退出了,但 ps 里还能看到它,状态是 Z,这是怎么回事?有危害吗?

**答**:子进程死后内核保留其退出状态等父进程 wait 认领,这个残壳就是僵尸,占 pid 与进程表槽位但不占内存。

- 实测死后 ps 显示 Z,waitpid 收尸后消失;

- 大量僵尸会耗尽 pid,进程表满后系统无法创建新进程;

- 服务端管 worker 的常规手法:SIGCHLD 处理或 WNOHANG 轮询收尸;

- 父进程先死则僵尸转交 init/launchd,由它收尸。

```python
# file: code/02_并发与网络工程/q2129_zombie.py
# -*- coding: utf-8 -*-
"""僵尸进程: 子进程死后没人 wait 的后果。

- 子进程先死, 内核保留其退出状态等父进程 wait, 这个残壳就是僵尸 Z;
- 僵尸不占内存但占用 pid 与进程表槽位, 大量僵尸会耗尽 pid;
- waitpid 收尸即可清除; 父进程先死则由 init/launchd 接管收尸。
"""
import os
import subprocess
import time


def zombie_stat(pid):
    r = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)],
                       capture_output=True, text=True)
    return r.stdout.strip() or "<gone>"


def main():
    # 场景一: 子进程先死, 父进程迟迟不收尸
    pid = os.fork()
    if pid == 0:
        os._exit(7)                    # 子进程立刻退出, 状态无人认领
    time.sleep(0.2)
    print("子进程 %d 死后 stat: %s (Z 开头即僵尸)" % (pid, zombie_stat(pid)))
    _, status = os.waitpid(pid, 0)     # 收尸
    print("waitpid 拿到退出状态:", os.waitstatus_to_exitcode(status))
    print("收尸后 stat:", zombie_stat(pid))

    # 场景二: WNOHANG 轮询是服务端管理子进程的常规手法
    pid2 = os.fork()
    if pid2 == 0:
        time.sleep(0.3)
        os._exit(0)
    r = os.waitpid(pid2, os.WNOHANG)
    print("存活时 WNOHANG 返回:", r, "(0 表示还没退)")
    time.sleep(0.5)
    r2 = os.waitpid(pid2, os.WNOHANG)
    print("退出后 WNOHANG 返回:", r2, "(pid 与状态一次取走)")
    print("最终 stat:", zombie_stat(pid2))


if __name__ == "__main__":
    main()
```

**追问**:1) Python 的 subprocess 会产生僵尸吗?——只要调了 wait()/poll()/communicate() 就不会;只 Popen 不管才积累。2) 僵尸和孤儿进程的区别?——僵尸是"死了没收尸",父活;孤儿是"父先死",子被 init 收养,继续跑,不是坏状态。3) 僵尸的系统性危害与量级?——每个僵尸占一个 PID+进程表项:PID 耗尽(默认 32768 可调)后 fork 全失败,是「慢性容量事故」;高频短命子进程的服务(爬虫/CI runner)是高发区——监控按「Z 状态进程数」告警。4) 收尸的工程手法?——subprocess 正常用 wait/poll/communicate 就不会积(每 Popen 配对 wait);批量子进程用 SIGCHLD handler+WNOHANG 循环收尸;父进程退出后由 init/launchd 收养收尸(孤儿转收养不是坏事)——「收尸责任跟着父进程走」。5) 生产陷阱?——Popen 只 spawn 不 wait(积僵尸);wait 阻塞主流程(用 WNOHANG 轮询);SIGCHLD handler 里做复杂逻辑(信号安全);僵尸与孤儿混淆(孤儿继续跑不是坏状态,僵尸必须收);容器里 PID 1 无收尸能力(要 tini/init)。

---
