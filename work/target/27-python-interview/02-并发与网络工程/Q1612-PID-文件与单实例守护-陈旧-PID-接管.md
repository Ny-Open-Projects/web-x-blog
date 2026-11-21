---
title: [Q1612] PID 文件与单实例守护:陈旧 PID 接管
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1612 · PID 文件与单实例守护:陈旧 PID 接管

> 难度:★★☆☆ | 标签:运维, PID 文件, 单实例

**问**:服务启动前怎么确保没有第二个自己?上次崩溃留下的 PID 文件怎么处理?

**答**:启动时用 O_CREAT 加 O_EXCL 独占创建 PID 文件——文件已存在说明有人先到。接着读出 PID 做探活:kill 传信号 0,不发信号只查存活;活着(或 EPERM——无权发信号但进程在)就拒绝启动;ESRCH(PID 已死)说明文件是上次崩溃留下的垃圾,unlink 后重新抢占接管。三个细节:EPERM 也要算活着,否则多用户机器上会误判;写 PID 用 O_EXCL 的 fd,避免先创建后写的历史窗口;探活与 unlink 之间存在竞态窗口,严格场景配合文件锁。

```python
# file: code/02_并发与网络工程/q1612_pidfile_guard.py
"""PID 文件与单实例守护: 陈旧 PID 接管。

防重复启动的轻量方案: 启动时 O_CREAT|O_EXCL 独占创建 PID 文件。
- 文件已存在: 读出 PID, 用 kill(pid, 0) 探活 -> 活着就拒绝启动;
- PID 已死(ESRCH): 文件是上次崩溃留下的垃圾 -> 接管;
- EPERM: 进程活着但无权发信号, 同样算活着。
注意 kill(pid, 0) 检查与 unlink 之间存在竞态窗口, 严格场景要配合文件锁。
"""
import errno
import os
import subprocess
import tempfile


class PIDFileBusy(Exception):
    def __init__(self, pid):
        super().__init__("已有实例在跑, PID=%d" % pid)
        self.pid = pid


def read_pid(path):
    with open(path) as f:
        text = f.read().strip()
    return int(text) if text else 0


def pid_alive(pid):
    if pid <= 0:
        return False
    try:
        os.kill(pid, 0)                 # 信号 0: 只探活, 不发送
        return True
    except OSError as e:
        return e.errno == errno.EPERM   # 活着但无权探查, 也算活


def acquire(path):
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        with os.fdopen(fd, "w") as f:
            f.write(str(os.getpid()))
        return "acquired"
    except FileExistsError:
        pid = read_pid(path)
        if pid_alive(pid):
            raise PIDFileBusy(pid)
        os.unlink(path)                 # 陈旧 PID: 清理垃圾后接管
        print("陈旧 PID=%d 已死, 接管 PID 文件" % pid)
        return acquire(path)


def main():
    path = os.path.join(tempfile.mkdtemp(prefix="q1612_"), "app.pid")

    r1 = acquire(path)
    print("第一次启动:", r1)
    assert r1 == "acquired"
    assert read_pid(path) == os.getpid()

    try:
        acquire(path)
        raise AssertionError("重复启动应被拒绝")
    except PIDFileBusy as e:
        print("第二次启动被拒:", e)

    # 制造一个真实的"已死 PID": 起一个立刻退出的子进程
    p = subprocess.Popen(["/bin/sleep", "0"])
    p.wait()
    dead_pid = p.pid
    assert not pid_alive(dead_pid), "该 PID 应已死亡"
    with open(path, "w") as f:
        f.write(str(dead_pid))          # 模拟上次崩溃留下的陈旧 PID 文件
    r3 = acquire(path)
    print("陈旧文件后的启动:", r3)
    assert r3 == "acquired", "陈旧 PID 文件应被接管"

    os.unlink(path)
    print("结论: O_EXCL 抢占 + kill(pid,0) 探活 + 死 PID 接管, 三段式单实例")


if __name__ == "__main__":
    main()
```

**追问**:1) 容器里 PID 1 有什么特殊?——PID 1 不转发默认信号,必须自己装 SIGTERM 处理器;容器里 PID 文件意义减弱,编排层的单实例语义替代它。2) kill(pid, 0) 探活的三种返回怎么处理?——0=活着;ESRCH=死了(PID 可接管);EPERM=活着但无权发信号(多用户机器),必须算活着——漏了 EPERM 会在共享主机上误判并抢跑双实例。3) 「探活与 unlink 竞态」怎么收口?——严格场景用 flock(文件锁)包裹「探活→unlink→重新创建」全程;或用「O_EXCL 创建+写 PID」原子序列(先创建后写的历史窗口要用临时文件+replace);容器/K8s 场景改用编排层的单实例语义( leader election)。4) 生产陷阱?——PID 文件只写不删(正常退出也要清理,atexit/信号处理);EPS/EPERM 混判;PID 复用(死进程 PID 被新进程复用,探活误判活着——加进程启动时间/名字核对);容器里依赖 PID 文件而 PID 1 语义特殊(Q1612 原问)。

---
