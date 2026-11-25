---
title: "[Q5757] set_wakeup_fd 与 self-pipe：信号处理器能做什么、如何安全唤醒事件循环"
date: 2026-11-25
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5757 · set_wakeup_fd 与 self-pipe：信号处理器能做什么、如何安全唤醒事件循环

难度：P7 ｜ 标签：signal、set_wakeup_fd、self-pipe、EINTR、事件循环、信号安全、主线程

**问**：自研事件循环用 `select` 阻塞等 IO，收到 SIGTERM 后要优雅停机。代码在 handler 里直接改全局变量、关连接、写日志，结果偶发"停机卡死"或"日志写到一半丢了"；后来改成 `signal.set_wakeup_fd(pipe_w)`，又遇到 `ValueError: the fd must be in non-blocking mode`。Python 的 handler 到底在什么上下文执行？为什么不能在里面做重活？`set_wakeup_fd` 和 self-pipe 的分工是什么？

**答**：

- **结论**：CPython 的 Python 级 handler **不在真正的信号上下文（async-signal context）里执行**：C 层的信号处理器只设置一个标志/写 wakeup fd，真正的 Python 回调是在**主线程**执行字节码的间隙、由求值循环的 "pending call" 检查调用的。所以在 handler 里可以分配对象、打日志、加锁——不会像 C 的 async-signal-safe 限制那样立刻崩；但它仍然**打断主线程**：handler 执行期间主线程不能干别的，做重活（连数据库、等锁、flush 大量日志）会阻塞整个事件循环，甚至死锁（handler 里等一把被主线程自己持有的锁）。`set_wakeup_fd(fd)` 的作用是：信号到达时，C 层往这个 fd 写一个字节（值是信号编号），让阻塞在 `select`/`poll` 的主循环立刻返回；它**不安装 handler**，也不替代你的 Python 回调，fd 必须是**非阻塞**的（否则写可能阻塞在信号上下文里，Python 直接拒绝），且只能在主线程设置。self-pipe 就是"用一根管道把信号变成 IO 事件"，让事件循环用统一的方式处理。

- **取舍**：a) handler 里只做"最小动作"：置一个 `threading.Event`/写一个字节/`loop.call_soon_threadsafe`，真正的清理放到事件循环或主循环里做；b) 用 `set_wakeup_fd` 而不是在 handler 里直接操作业务：前者把"信号"转成"fd 可读"，与 select/poll/epoll 的等待模型天然契合，也不会在 handler 里做 IO；c) 用 `asyncio.add_signal_handler` 而不是手写 self-pipe：它内部已经做了 wakeup fd + `call_soon_threadsafe`，还能在回调里直接 `await` 清理逻辑；手写只适合非 asyncio 的自研循环；d) 别用 `signal.signal` 的 handler 去 flush 日志/关闭连接池：这些操作可能拿锁、可能阻塞，应该由主循环在"安全点"执行；e) Windows 上没有 `set_wakeup_fd` 的完整语义（只支持 socket），跨平台用 `add_signal_handler` 或 `ProactorEventLoop` 的能力。

- **实战**：事故形态是"K8s 发 SIGTERM 后进程偶尔卡到 SIGKILL"——handler 里同步调用了"关闭连接池"（等所有连接归还，最长 30s），而主线程此时正持有连接池的锁在写数据；handler 在主线程执行，等锁 → 自己等自己 → 死锁。修复：handler 只 `stop_event.set()`，主循环醒来后按"停收新连接 → 排空 → 关池 → 退出"的顺序做；同时用 `set_wakeup_fd` 保证 `select` 能被打断（否则 handler 要等到下一次 IO 才执行）。第二个坑是"日志丢半行"：handler 里用 `logging`（内部有锁 + IO），信号频繁时日志交错；改成 handler 只写一个字节/计数，日志由主循环统一打。

```python
# Python handler 在主线程字节码间隙执行; set_wakeup_fd 把信号变成可读 fd
import os
import signal
import socket
import threading
import time

read_fd, write_fd = socket.socketpair()

blocking_err = ""
try:
    signal.set_wakeup_fd(write_fd.fileno())      # 写端必须非阻塞
except ValueError as e:
    blocking_err = str(e)
    print("→ 阻塞 fd 被拒绝:", e)
assert "non-blocking" in blocking_err

read_fd.setblocking(False)
write_fd.setblocking(False)
old_fd = signal.set_wakeup_fd(write_fd.fileno())

seen = []
def handler(signum, frame):
    seen.append((signum, threading.current_thread().name))

signal.signal(signal.SIGUSR1, handler)

def sender():
    time.sleep(0.01)
    os.kill(os.getpid(), signal.SIGUSR1)

threading.Thread(target=sender).start()

# 主线程在纯 Python 循环中: handler 会在字节码间隙插入执行
count = 0
while not seen:
    count += 1
print("→ handler 触发前主线程循环了", count, "次, 执行线程:", seen[0][1])
assert seen[0][0] == signal.SIGUSR1
assert seen[0][1] == "MainThread"        # 只投递到主线程
assert count > 0                          # 循环执行到一半被打断, 不是等循环结束

# 信号编号被写入 wakeup fd, 事件循环靠这个字节醒来
read_fd.settimeout(1.0)
data = read_fd.recv(1)
print("→ wakeup fd 读到的字节:", data[0], "等于信号编号:", data[0] == signal.SIGUSR1)
assert data == bytes([signal.SIGUSR1])

# handler 里只做最小动作, 重活交给主循环
stop = threading.Event()
def light_handler(signum, frame):
    stop.set()                            # 唯一动作: 置标志

signal.signal(signal.SIGTERM, light_handler)
os.kill(os.getpid(), signal.SIGTERM)
assert stop.is_set()
print("→ 轻量 handler 只置标志, 清理逻辑由主循环执行")

signal.set_wakeup_fd(old_fd)
signal.signal(signal.SIGUSR1, signal.SIG_DFL)
signal.signal(signal.SIGTERM, signal.SIG_DFL)
read_fd.close()
write_fd.close()
```

**追问一**：既然 Python handler 不在信号上下文执行，为什么还说"不能做重活"？—— 两个层面：①**执行位置**：handler 在主线程的字节码间隙运行，此时它**取代**了主线程正在做的事——如果主线程是事件循环，handler 执行多久，循环就停多久，所有连接的读写都被推迟；如果 handler 里等一把锁，而这把锁正被主线程自己持有（比如在 `with pool.lock:` 中间收到信号），就是自死锁。②**可重入性**：handler 可能在任意字节码边界插入，如果它修改了主逻辑正在遍历的容器（dict/list），会触发 "dictionary changed size during iteration" 或更隐蔽的状态不一致。所以纪律是"handler 只做幂等的标志位/单字节写"，把状态变更收敛到主循环的一个安全点。C 层的 async-signal-safe 限制（只能调 `write` 等）在 Python 层被放宽了，但**并发安全**的约束没有放宽。

**追问二**：self-pipe 和 `set_wakeup_fd` 有什么区别？为什么 fd 必须非阻塞？—— self-pipe 是一种**模式**：创建一根管道（或 socketpair），信号 handler 往里写，主循环 select 读端；`set_wakeup_fd` 是**帮你完成写动作的机制**：它让 C 层在信号到达时自动往指定 fd 写信号编号，你不需要在 Python handler 里 `os.write`（也就避免了"handler 还没跑，select 还在睡"的窗口）。fd 必须非阻塞，是因为写发生在信号投递路径上：如果管道满了（信号风暴），阻塞写会让进程卡在信号处理里，甚至死锁；非阻塞写最坏是丢掉这个字节——信号本来就会合并，丢字节可以接受，Python 会打一条 "Exception ignored when trying to write to the signal wakeup fd" 的警告。另一个要求是"用原始 fd"：不要传 `open(..., 'w')` 的缓冲文件对象，缓冲层会把字节攒在用户态，select 永远等不到。

## 背诵要点

- Python handler 在主线程字节码间隙执行（非 C 信号上下文）：可以分配/打日志，但会阻塞主线程，重活与等锁会导致循环停顿或自死锁。
- `set_wakeup_fd(fd)` 在信号到达时自动写一个信号编号字节以唤醒 select/poll；fd 必须非阻塞、主线程设置，它不安装 handler。
- 正确姿势：handler 只置标志/写字节，清理在主循环安全点做；asyncio 用 `add_signal_handler`，自研循环用 self-pipe + wakeup fd。

## 复盘追问

- 为什么 handler 里"关闭连接池"可能死锁？（handler 在主线程执行，若主线程正持有连接池的锁，handler 等同一把锁 = 自己等自己）
- 为什么 wakeup fd 一定要非阻塞，满了会怎样？（写发生在信号投递路径，阻塞写会卡死进程；非阻塞最多丢字节，信号本来可合并）
