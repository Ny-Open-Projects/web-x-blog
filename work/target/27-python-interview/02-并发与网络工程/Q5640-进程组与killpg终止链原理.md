---
title: [Q5640] 进程组与 killpg：进程树终止的信号原理
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5640 · 进程组与 killpg：进程树终止的信号原理

难度：P6-P7 | 标签：killpg、进程组、setsid、原理深挖、subprocess

**问**：用 `subprocess.Popen` 起的外部命令自己又 fork 了子进程，`proc.terminate()`（SIGTERM）只杀了直接子进程，孙进程还活着继续占端口/写文件。为什么会这样？进程组/会话（process group / session）机制如何解决？优雅终止链 terminate→kill→wait 应该怎样实现？

**答**：

**结论**：信号是按 PID 单播的：`proc.terminate()` = `os.kill(pid, SIGTERM)`，只到达直接子进程；孙进程（外部命令内部 fork 出来的，如 shell 脚本起的后台进程）不受影响，且失去父进程后被 init/pid1 收养继续运行。解决方案是把"一棵进程树"放进同一**进程组**：`Popen(start_new_session=True)`（调 setsid，新会话+新进程组，组长=子进程 PID），终止时 `os.killpg(os.getpgid(proc.pid), SIGTERM)` 一次性发给整组。会话与进程组的意义：(1) 组内广播信号；(2) 控制终端把 Ctrl-C/SIGHUP 发给前台组；(3) setsid 脱离终端后 SIGHUP 不再误达。

**取舍**：优雅终止链的标准模板：先 SIGTERM 给组 → 短超时（3-10s）wait → 未退则 SIGKILL 给组 → 再 wait → 收割僵尸。注意三个坑：(1) killpg 必须在子进程仍持有其进程组时调用，若子进程已退出且孙进程被收养，getpgid 会失败——先 killpg 再 join，异常兜底；(2) SIGKILL 不给清理机会，可能留下锁文件/共享内存，生产尽量让 SIGTERM 阶段跑完；(3) macOS 上 pid1 语义与 Linux 容器不同，容器内 orphan 由容器 init（tini/--init）负责收割，不加 --init 就会僵尸堆积。

**实战**：验证实验用 sh 脚本 spawn 一个后台 sleep，对比单 PID terminate 与 killpg 的效果差异；生产里把"终止链"封装成统一的 `terminate_process_tree(proc, timeout)` 工具。

```python
import os, signal, subprocess, sys, time

# 外部命令：shell 起 3 个 sleep（孙进程）
cmd = ["sh", "-c", "sleep 300 & sleep 300 & sleep 300 & wait"]
proc = subprocess.Popen(cmd, start_new_session=True)   # 新会话+新进程组
time.sleep(0.5)

def tree_pids(root):
    """枚举进程组内的存活 pid（macOS/Linux 通用：ps -o pgid）。"""
    out = subprocess.run(
        ["ps", "-axo", "pid,pgid,command"], capture_output=True, text=True
    ).stdout.splitlines()
    pgid = os.getpgid(root)
    return [l for l in out if f" {pgid} " in l and "sleep" in l]

pids = tree_pids(proc.pid)
print("进程组内 sleep 进程数 =", max(0, len(pids)))

# 优雅终止链：SIGTERM 整组 -> 超时 -> SIGKILL 整组 -> wait
try:
    os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
except ProcessLookupError:
    pass
try:
    proc.wait(timeout=5)
    print("整组 SIGTERM 后已退出")
except subprocess.TimeoutExpired:
    print("超时，升级 SIGKILL")
    os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    proc.wait()
print("exit code =", proc.returncode)
time.sleep(0.5)
print("残留 sleep 进程数 =", max(0, len(tree_pids(proc.pid))) if proc.poll() is None else 0)
```

**追问 1**：`start_new_session=True` 与已废弃的 `preexec_fn=os.setsid` 有什么区别？
答：效果相同（子进程 setsid），但 preexec_fn 在 fork 后 exec 前的子进程里执行任意 Python 代码，多线程父进程下不安全（信号/锁状态未定义），3.2+ 提供专用参数替代；POSIX spawn 路径下 preexec_fn 直接不可用。

**追问 2**：为什么容器内 PID 1 进程（Python 应用本身）默认不收割孤儿？
答：PID 1 的默认信号处置被内核特殊化（未显式注册 handler 的信号被忽略），且它不是 init，没有自动 reap orphan 的行为；子进程变僵尸堆积直到显式 wait——所以容器化 Python 服务要么用 tini/--init，要么应用自己定期 waitpid(-1)。

**追问 3**：进程组与 cgroup 的终止语义差异？
答：killpg 是信号广播，进程可以忽略/捕捉 SIGTERM；cgroup freezer/kill 是内核级（freeze 或 SIGKILL 所有进程），容器停止走 cgroup 兜底——这也是"SIGTERM 阶段必须限时，超时由编排层 SIGKILL"的分层依据。

## 背诵要点

- 信号按 PID 单播，terminate 只杀直接子进程；start_new_session=True + killpg 才能清整棵树。
- 终止链：SIGTERM 组 → 限时 wait → SIGKILL 组 → wait 收割；killpg 有 ProcessLookupError 兜底。
- 容器 PID 1 不收养不 reap：用 --init 或自管 waitpid(-1)；cgroup 兜底 SIGKILL 与优雅停机分层。

## 复盘追问

- 如何设计一个可复用的 terminate_process_tree 工具？(提示：组探测、双阶段、返回 exit code、指标上报)
- 为什么 SIGTERM 阶段超时上限要贴近下游排空时间而非固定 3 秒？(提示：与优雅停机窗口联动)
