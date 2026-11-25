---
title: "[Q5709] SIGCHLD 收尸抢走子进程：Popen 为什么把失败报成 0"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5709 · SIGCHLD 收尸抢走子进程：Popen 为什么把失败报成 0

难度：P7 ｜ 标签：SIGCHLD、waitpid、subprocess、Popen、僵尸进程、退出码

**问**：守护进程里装了 `SIGCHLD` 处理器，用 `os.waitpid(-1, WNOHANG)` 统一收尸；同一进程里又用 `subprocess.Popen` 跑任务，结果一个退出码 7 的失败任务，`p.poll()` 返回 0，监控完全没告警。谁把退出状态拿走了？`Popen` 遇到 `ECHILD` 为什么不当异常？两者能共存吗？

**答**：
结论：`waitpid(-1, ...)` 会回收**任意**已退出子进程，包括 `Popen` 创建的那个。`Popen` 之后调用 `waitpid(self.pid, WNOHANG)` 时子进程已被回收，内核返回 `ECHILD`；CPython 的 `_internal_poll` 在 `ECHILD` 且没有 `_deadstate` 时把 `returncode` 设成 **0**（历史上为了兼容"子进程已被别人收走"的情况），于是失败被静默伪装成成功。

取舍：a) 不要在同一进程里同时用"全局 SIGCHLD 收尸"和 `subprocess.Popen` 管理子进程，职责冲突；b) 需要统一收尸的守护进程，子进程创建/回收都走自己的封装，记录 pid → 元数据，`waitpid` 只处理已知 pid，不要用 `-1` 盲收；c) 必须用 `Popen` 时，把 SIGCHLD 处理器设为"只唤醒、不 waitpid"，让 `Popen.poll()` 自己收；d) 需要非破坏性观察，用 `os.waitid(P_PID, pid, WEXITED | WNOWAIT)`，看完状态不摘除，仍由 Popen 收；e) 双 fork 的守护进程不产生可直接 wait 的子进程，和 Popen 是两种模型，别混。

实战：事故形态是"任务调度器用 SIGCHLD 统一回收 runner 子进程，同时用 Popen 跑数据校验；校验脚本退出码非 0 时被 SIGCHLD 先收走，Popen 报 0，坏数据被当成通过，直到对账才发现"。下面演示抢尸：真实退出码 7，Popen 却返回 0。

```python
import os
import subprocess
import sys
import time

p = subprocess.Popen([sys.executable, "-c", "raise SystemExit(7)"])

pid, status = 0, 0
for _ in range(50):
    pid, status = os.waitpid(-1, os.WNOHANG)   # 模拟 SIGCHLD 里的盲收
    if pid:
        break
    time.sleep(0.02)

real_code = os.waitstatus_to_exitcode(status) if pid else None
print("[1] 被外部 waitpid 收走:", pid == p.pid, "真实退出码:", real_code)
print("[2] Popen.poll() 看到:", p.poll())
print("[3] Popen.returncode 被写成:", p.returncode)
print("[4] 失败被伪装成成功:", real_code == 7 and p.returncode == 0)
```

**追问一**：为什么 CPython 不直接抛 `ChildProcessError`？—— 早期实现里 `Popen` 需要容忍"子进程被外部 SIGCHLD 处理器收走"的部署方式，抛异常会让大量守护进程崩溃；于是选择把 `returncode` 设为 0（`_deadstate` 为 None 时）。这是一个"兼容优先"的取舍，代价是静默错误。3.x 各版本行为基本一致，别指望升级 Python 修复。

**追问二**：怎么安全地"看一眼退出状态但不抢走"？—— Linux/macOS 支持 `os.waitid(os.P_PID, pid, os.WEXITED | os.WNOWAIT)`，它返回 `siginfo` 但不摘除僵尸，之后 `Popen.wait()` 仍能拿到真实状态；不是所有平台都支持 `WNOWAIT`，要做兼容判断。更稳的做法是根本不让第二个回收者存在：SIGCHLD 处理器只做 `self-pipe` 唤醒，真正 `waitpid` 集中在事件循环/Popen 一处。

## 背诵要点
- `waitpid(-1)` 会抢走 Popen 的子进程；Popen 遇 `ECHILD` 把 `returncode` 设为 0，失败静默变成功。
- 不要混用全局 SIGCHLD 收尸与 Popen；SIGCHLD 只唤醒不 wait，或自己维护 pid 白名单。
- 非破坏性观察用 `waitid(..., WNOWAIT)`；跨平台要判断支持。

## 复盘追问
- 退出码 7 的任务为什么监控显示成功？（ECHILD → returncode=0）
- 守护进程既要收尸又要 Popen，怎么设计才不冲突？（单一回收者 / pid 白名单 / WNOWAIT）
