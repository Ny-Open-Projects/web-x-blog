---
title: "[Q5702] resource.setrlimit：给子进程划资源上限的正确姿势"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5702 · resource.setrlimit：给子进程划资源上限的正确姿势

难度：P6 ｜ 标签：resource、setrlimit、RLIMIT_NOFILE、子进程、沙箱、软硬限制

**问**：调度器要跑用户提交的脚本，担心它打开上万文件或吃光内存。`ulimit` 是 shell 层的，Python 里怎么给单个子进程设资源上限？软限制和硬限制分别是什么？为什么 `preexec_fn` 里设限制比在子进程脚本里自己设更早、更安全？`RLIMIT_AS` 为什么在部分平台上不生效？

**答**：
结论：标准库 `resource.setrlimit(resource, (soft, hard))` 设置单个进程的资源上限；软限制是当前生效值（可自行调低或升到硬限制），硬限制是不可逾越的天花板（普通进程只能降不能升，需要特权才能升）。给子进程设限的两种时点：a) 父进程在 `subprocess.Popen(preexec_fn=...)` 或 fork 后 exec 前设置——限制在**任何用户代码运行前**生效，能挡住"脚本第一行就疯狂 fork"这类攻击；b) 子进程脚本开头自己 `setrlimit`——只对之后的代码生效，之前的 import 已经花了资源。限制触发时表现为 `OSError`（如 `EMFILE`）、`MemoryError` 或被信号杀死（如 CPU 超限 `SIGXCPU`）。

取舍：a) `RLIMIT_NOFILE` 最常用也最可靠，跨 macOS/Linux 行为一致；`RLIMIT_AS` 在 macOS 上定义为常量但内核基本不执行，内存上限在容器里应该交给 cgroup，Python 层只做辅助；b) 软=硬时子进程无法再放宽，适合完全不可信代码；软<hard 留余量时，允许可信子进程自我调节；c) `preexec_fn` 在有线程的父进程里不安全（3.12 已对含线程场景警告），更稳的形态是 fork+exec 自己控制，或用 `subprocess` + 一次性 `resource.prlimit`（Linux）；d) 限制不是沙箱，只是"事故半径"：文件系统、网络、进程间信号都要另设边界。

实战：事故形态是"批处理 worker 跑用户脚本，脚本里 `open()` 循环泄漏，fd 打满整机 10 万上限，同机其他服务跟着遭殃；给子进程设 `RLIMIT_NOFILE` 软硬均 64 后，泄漏脚本只烧掉自己 64 个 fd，`EMFILE` 快速失败，其他进程无感"。下面演示子进程自我设限后被 `EMFILE` 挡住。

```python
import subprocess
import sys

child = (
    "import resource, os\n"
    "resource.setrlimit(resource.RLIMIT_NOFILE, (10, 64))\n"
    "fds = []\n"
    "try:\n"
    "    for i in range(20):\n"
    "        fds.append(open('/dev/null', 'w'))\n"
    "    print('all opened, no limit hit')\n"
    "except OSError as e:\n"
    "    print('blocked: extra fds =', len(fds), 'errno =', e.errno)\n"
)

p = subprocess.run([sys.executable, "-c", child], capture_output=True, text=True)
print("[1]", p.stdout.strip())
print("[2] 子进程退出码:", p.returncode)
```

**追问一**：为什么要在 exec 前设限制，而不是让子进程自己设？—— 时序决定防护面。exec 前设置，限制覆盖从第一条用户指令开始的所有行为，包括 import 的 fd 消耗和 fork；脚本内自设只能保护"后半程"。极端例子：脚本 import 一个恶意包，包在 import 时就 `os.fork` 上千个进程，自设方案根本没机会执行。代价是 `preexec_fn` 在多线程父进程里有 fork 安全风险，需要权衡或改用 Linux 的 `prlimit` 外部命令。

**追问二**：软限制和硬限制在救援场景怎么配合？—— 软限制触发告警（如 `SIGXCPU` 在软 CPU 时间先到时发出），硬限制是止损底线。运维常用"软 = 目标值 × 0.9，硬 = 目标值"：软限制触发的信号先打日志/上报，真到硬限制才硬失败。普通进程可以 `setrlimit(soft, hard)` 在软硬之间上调软限制，但不能超过硬限制；只有 root（或 CAP_SYS_RESOURCE）能抬硬限制，所以父进程给子进程的硬限制就是它一生的天花板。

## 背诵要点
- `setrlimit(res, (soft, hard))`：软限制是生效值可调，硬限制是不可逾越的天花板；普通进程只能降硬限制。
- exec 前设限制（preexec_fn/fork）覆盖全程用户代码，脚本内自设只保后半程；preexec_fn 多线程父进程不安全。
- `RLIMIT_NOFILE` 跨平台可靠；`RLIMIT_AS` macOS 不执行，内存上限交给 cgroup；触发形态是 OSError/MemoryError/信号。

## 复盘追问
- 为什么脚本开头自己 setrlimit 防不住 import 恶意包？（限制在用户代码后才生效，import 已消耗资源）
- RLIMIT_AS 设了为什么 macOS 上没效果？（内核不执行，容器内存上限应交 cgroup）
