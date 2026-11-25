---
title: "[Q5714] SIGALRM 硬超时守卫：setitimer、可打断点与线程边界"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5714 · SIGALRM 硬超时守卫：setitimer、可打断点与线程边界

难度：P7 ｜ 标签：SIGALRM、setitimer、硬超时、signal、主线程限制、C 扩展超时

**问**：普通超时靠线程/异步取消，为什么还需要 SIGALRM？time.sleep(10) 能被 SIGALRM 打断吗？死循环的纯 Python 代码和阻塞在 C 扩展里的代码，哪个能被信号打断？为什么 signal 只能在主线程设置——线上服务怎么绕开这个限制？

**答**：
结论：`signal.setitimer(ITIMER_REAL, seconds)` 让内核在到期时向进程发 **SIGALRM**，处理器在主线程的字节码间隙执行 Python handler——这是**唯一能打断"不配合取消"代码**的机制：线程取消要目标代码自己检查标志，asyncio 取消只在 await 点生效，而一个死循环或阻塞在 C 扩展里的调用对这些都无感。SIGALRM 打断面：`time.sleep`/`socket` 等系统调用阻塞点会被信号唤醒（PEP 475 会重试系统调用，但若 handler 抛异常则直接传播出来），纯 Python 死循环在字节码间隙能收到信号并抛出 handler 的异常；**C 扩展内部长时间不返回则打不断**（信号要等它回到 Python 层才被处理）——这是硬超时的能力边界。线程限制：Python 的 signal handler 只在主线程注册与执行（C 信号处理器的执行线程就是内核指定的主线程），工作线程里 `setitimer` 无效。服务端绕法：信号守卫只在主线程执行（入口协程/主循环发起，配合 loop.run_in_executor 的任务用 future 超时替代），或用子进程隔离 + 外部 kill。

取舍：a) 适用：单次批处理脚本、迁移命令、调试卡死——进程级"最后防线"；b) 不适用：多线程服务里给工作线程上闹钟（无效），给 Web 请求上 SIGALRM（会污染全局计时器，一个进程只有一个 ITIMER_REAL）；c) handler 抛异常是打断的标准姿势（TimeoutError），但异常会从任意字节码位置冒出——被保护代码里的 try/except Exception 可能吞掉它，所以 TimeoutError 别放在被宽捕获吞掉的位置，或用不可捕获的思路（标记 + 外层统一检查）；d) 嵌套超时不支持：一个进程只有一个 real 秒表，嵌套场景要靠子进程隔离；e) 与 asyncio 的关系：事件循环有自己的定时器，SIGALRM 在 loop 里反而会打断 select/poll（loop 有 EINTR 处理），混用要格外小心——loop 场景用 `asyncio.wait_for`，SIGALRM 留给"没有异步化的裸阻塞调用"。

实战：事故形态是"数据修复脚本卡在一个第三方 C 扩展的解析函数上（内部死循环），kill -9 才能退出且丢失进度；包一层 SIGALRM 硬超时 + 分块调用，每块 10 秒上限，超时保留已完成块"。下面验证打断行为与线程边界。

```python
import signal
import threading
import time

print("[1] 当前是主线程:", threading.current_thread() is threading.main_thread())


def hard_guard(seconds, fn, *args):
    """主线程硬超时守卫: SIGALRM 打断不配合取消的代码"""
    if threading.current_thread() is not threading.main_thread():
        raise RuntimeError("SIGALRM 守卫只能在主线程使用")

    def handler(signum, frame):
        raise TimeoutError(f"hard timeout {seconds}s")

    old = signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    t0 = time.perf_counter()
    try:
        return fn(*args)
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)  # 复位: 防止守卫泄漏到后续代码
        signal.signal(signal.SIGALRM, old)


def slow():
    time.sleep(30)


try:
    hard_guard(0.05, slow)
except TimeoutError as e:
    print("[2] sleep 被硬超时打断:", e)


def busy_loop():
    n = 0
    while True:          # 纯 Python 死循环: 字节码间隙可收信号
        n += 1


try:
    hard_guard(0.05, busy_loop)
except TimeoutError as e:
    print("[3] 死循环被打断:", e)
print("[4] 定时器已复位, 进程正常收尾")
```

**追问一**：为什么死循环能被打断而 C 扩展死循环不能？—— Python 3.10+ 的字节码求值循环每条指令间会检查 pending signals（`_PyEval_EvalFrameDefault` 里的 eval breaker）：SIGALRM 到达 → C 级 handler 置标志 → 主线程在两条字节码之间调用 Python handler → 抛 TimeoutError。C 扩展执行期间控制权不在解释器循环里，标志位要等扩展返回后才检查——扩展内部死循环 = 永远不返回 = 打不断。对策只剩进程隔离：把可疑调用放子进程，父进程 `proc.join(timeout)` + kill（注意 Q5185 的管道坑）。这也解释了 faulthandler 的 dump_dot 价值：至少能在超时前把栈转出来（Q1836）。

**追问二**：多线程服务怎么实现"C 扩展级硬超时"的等价物？—— Python 线程模型给不出答案（线程不可强杀），等价物是**进程池 + 超时回收**：`ProcessPoolExecutor` 的任务超时后无法真正终止 worker，正确做法是 kill 掉整个 worker 进程并重建池（或用 multiprocessing.Process + terminate）。成本是任务状态丢失与池重建开销，所以设计上要把"可能失控的第三方调用"隔离在**独立的无状态 worker**里，与主服务池分开——这正是舱壁模式（Q1876）在超时维度的应用：隔离的不只是资源，还有故障半径。

## 背诵要点
- SIGALRM + setitimer 是唯一能打断"不配合取消"代码的机制；time.sleep 与字节码循环可打断，C 扩展内部打不断。
- 信号 handler 只能在主线程注册与执行；一个进程只有一个 ITIMER_REAL，不支持嵌套。
- C 扩展失控的等价方案 = 子进程/独立 worker + terminate；finally 里必须复位定时器防泄漏。

## 复盘追问
- 第三方 C 扩展死循环卡死脚本，SIGALRM 为什么也救不了？（控制权不在解释器循环；子进程隔离 + terminate）
- 多线程 Web 服务能否给单请求上 SIGALRM？（不能：主线程限制 + 全局唯一计时器；用进程池/任务级超时）
