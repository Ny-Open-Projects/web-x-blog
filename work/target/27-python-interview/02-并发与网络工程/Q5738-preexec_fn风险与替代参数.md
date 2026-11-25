---
title: "[Q5738] subprocess preexec_fn 的风险与替代：fork 与 exec 之间的危险窗口"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5738 · subprocess preexec_fn 的风险与替代：fork 与 exec 之间的危险窗口

难度：P6 ｜ 标签：preexec_fn、fork、exec、setsid、死锁窗口、start_new_session、process_group、subprocess 安全

**问**：`preexec_fn` 在子进程的什么阶段执行？为什么官方文档说"多线程程序里用它有死锁风险"？`start_new_session=True`、`process_group=0`（3.11+）等替代参数覆盖了哪些常见需求？什么时候真的必须用 preexec_fn、怎么把风险压到最低？

**答**：
结论：`preexec_fn` 是一个在 **fork 之后、exec 之前**的窗口里于子进程内执行的 Python 回调——这个窗口是 CPython 与 POSIX 都明确标注的危险区：①子进程此刻**只有调用线程**，但父进程的锁状态被原样复制——若 preexec_fn 触碰任何"父进程其它线程正持有的锁"（内存分配器锁、logging 锁、import 锁），子进程将永久死锁；②窗口内**不能用任何可能加锁/分配的操作**——调用 Python 函数本身就有解释器行为，官方文档的警告"as little as possible in the child"就是对这两点的浓缩；③exec 失败时错误要穿过这个窗口传回父进程，进一步放大复杂度。常见需求几乎都有**专用参数替代**：改会话/脱离终端用 `start_new_session=True`（等价 setsid）、改进程组用 `process_group=0`（3.11+）、改用户/组用 `user=`/`group=` 参数、改环境用 `env=`、限资源用 `rlimit=` 家族或启动后由子进程自己做——**能用参数就不用回调**。真正必须 preexec_fn 的场景很少（如设置特殊 namespace、恢复自定义信号 disposition），且要遵守三条纪律：回调只调 OS 级 C 函数（os 模块的无分配子集）、绝不碰 Python 层全局状态、回调内失败只能 os._exit 不能 raise（异常传播路径同样要穿过窗口）。

取舍：a) 95% 的"改会话/进程组/用户"需求：start_new_session/process_group/user/group 参数——语义由 subprocess 在 C 层实现，无窗口风险；b) 需要复杂子进程初始化：改成**子进程入口自己初始化**（python -c 包一层），把窗口内操作挪到 exec 后，失败路径清晰；c) 3.11+ 的 subinterpreters 环境、Py_GIL_DISABLED（自由线程）环境：preexec_fn 被直接禁止/强烈劝退——历史包袱正在收缩；d) 确需要用时的降险：回调最小化到纯 syscall、不 import、不调 logging、线程态父进程改用 spawn/forkserver 起子进程链再在其中做初始化；e) 与 fork 继承家族（Q5560 fd 继承、Q2125 缓冲重复输出）联动：close_fds=True 默认已是防线，preexec_fn 里不要再手工搅动 fd。

实战：事故形态是"多线程调度服务用 preexec_fn 在子进程里调 logging 初始化（写配置加载），恰逢父进程其它线程持 logging 锁——子进程复制了持锁状态，在窗口内永久卡死，表现为 spawn 的 worker 100% 卡住且 kill 不掉；修复为 start_new_session=True + 子进程入口自初始化，窗口内零 Python 调用"。下面实测参数替代路径与最小化回调。

```python
# preexec_fn 的风险与替代参数
import os
import subprocess
import sys

code_probe = "import os; print('sid=%d pid=%d' % (os.getsid(0), os.getpid()))"

print("[1] 替代参数一: start_new_session=True (等价 setsid, 不经过 preexec_fn 窗口)")
r = subprocess.run([sys.executable, "-c", code_probe],
                   start_new_session=True, capture_output=True, text=True)
out1 = r.stdout.strip()
print("   ", out1)
print("    sid == pid (新会话组长)?", out1.split("sid=")[1].split()[0] == out1.split("pid=")[1].split()[0])

print("[2] 对照: 不传参数 -> 继承父进程会话 (sid != pid)")
r2 = subprocess.run([sys.executable, "-c", code_probe], capture_output=True, text=True)
out2 = r2.stdout.strip()
print("   ", out2)

print("[3] 替代参数二: process_group=0 (3.11+, 子进程独立进程组, 不随父进程被信号连坐)")
if sys.version_info >= (3, 11):
    r3 = subprocess.run([sys.executable, "-c", "import os; print('pgid=%d pid=%d' % (os.getpgid(0), os.getpid()))"],
                        process_group=0, capture_output=True, text=True)
    print("   ", r3.stdout.strip(), "(pgid == pid: 自己是组长)")
else:
    print("    3.11 前用 preexec_fn=os.setpgrp 或 start_new_session=True 兜底")

print("[4] 必须用 preexec_fn 时: 回调最小化 (纯 syscall, 零 Python 全局状态)")
def minimal_preexec() -> None:
    os.umask(0o027)                          # 纯 syscall, 无锁无分配, 窗口内安全
r4 = subprocess.run([sys.executable, "-c", "import os; print('umask=%o' % (os.umask(0o022)))"],
                    preexec_fn=minimal_preexec, capture_output=True, text=True)
print("   ", r4.stdout.strip(), "(0o027 生效)")

print("[5] 反例说明: preexec_fn 里调 logging/import/配置加载 = 窗口内锁死 (多线程父进程)")
print("    危险窗口: fork 之后 exec 之前, 子进程只有调用线程 + 复制的锁状态")
print("[6] 纪律: 能用参数不用回调; 复杂初始化挪到子进程入口; 回调内失败 os._exit 不 raise")
```

**追问一**：为什么"fork 之后 exec 之前"的窗口这么危险？CPython 在这个窗口里默认还做了什么？—— 窗口危险的三层原因：①**单线程假象**——fork 复制整个地址空间，子进程"看起来"有全部状态，但只有调用线程活着：任何被其它线程持有的锁（malloc arena、GIL、logging、random 的内部锁）在子进程里永远是"被锁住"状态，窗口内一碰即死锁；②**async-signal-unsafety**——POSIX 规定 fork 与 exec 之间的代码只能调用 async-signal-safe 函数，而 Python 函数调用本身就要分配对象、可能触发 GC，理论上每一次 Python 调用都在越界；③**错误传播受限**——exec 失败时 CPython 靠预写的错误管道传回异常，preexec_fn 若抛异常也要走这条管道，窗口内状态不可靠时这层机制同样不可靠。CPython 默认在这个窗口做的动作被刻意压到最少：close_fds 关闭继承 fd、dup2 重定向 std 流——全是不可失败/极少失败的 syscall 级操作，这正是 preexec_fn 应该效仿的边界。

**追问二**：start_new_session、process_group、setsid 的信号语义差别是什么？"Ctrl+C 连坐"是怎么回事？—— 三者的信号语义：①**start_new_session=True**（setsid）：子进程脱离控制终端、成为新会话——终端产生的 SIGINT/SIGHUP/SIGQUIT **完全隔离**，交互式 Ctrl+C 打不到子进程；②**process_group=0**（setpgid(0,0)）：子进程独立进程组但仍在同一会话——Ctrl+C 会发给前台**进程组**，独立组后不再连坐，但会话级的 SIGHUP（终端关闭）仍会波及；③**setsid 完全脱离会话**——连 SIGHUP 都收不到，适合守护进程化。连坐事故形态：交互脚本用 subprocess 起了 10 个子任务，用户 Ctrl+C 想中止主脚本，SIGINT 发给整个前台进程组——10 个子任务同时被打断（而它们可能正在写盘），留下半成品状态。选型：后台任务不想被打断 → process_group=0 或 start_new_session；真守护进程 → start_new_session + SIGHUP handler 显式化；需要随父进程一起死的**前台协作任务** → 什么都不设（继承组），让 Ctrl+C 语义天然覆盖全家——"隔离"与"连坐"都是特性，按任务与父进程的生命周期绑定关系选。

## 背诵要点
- preexec_fn 在 fork 后 exec 前执行：窗口内只有调用线程+复制的锁状态，碰锁即死锁；只能调 async-signal-safe 级 syscall。
- 常见需求全有参数替代：start_new_session（setsid）/ process_group=0（3.11+，独立进程组）/ user/group/env/umask 用回调需最小化。
- 复杂初始化挪到子进程入口；回调内失败 os._exit 不 raise；信号隔离三档：独立组不连坐 Ctrl+C、setsid 连 SIGHUP 都隔离。

## 复盘追问
- 多线程服务里 preexec_fn 初始化 logging 为什么卡死？（窗口内复制父进程持锁状态，logging 锁永不可得；改 start_new_session+入口自初始化）
- Ctrl+C 把子任务一起打断怎么选参数？（process_group=0 防连坐；setsid 彻底脱离终端；前台协作任务保留继承组）
