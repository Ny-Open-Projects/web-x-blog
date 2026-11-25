---
title: "[Q5201] os.register_at_fork：fork 之后子进程必须重置什么"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5201 · os.register_at_fork：fork 之后子进程必须重置什么

难度：P7 ｜ 标签：fork、register_at_fork、连接池、锁、preload、COW

**问**：Gunicorn `--preload` 启动后，子进程偶尔在第一次请求时永久卡住，`py-spy` 显示卡在 `logging` 的锁上；另一个服务 fork 后所有 worker 共用同一个数据库连接，查询互相串包。`os.register_at_fork` 能解决什么？`before`/`after_in_parent`/`after_in_child` 分别在什么时机跑？为什么"fork 后重置锁"不是万能药？

**答**：
结论：`fork()` 只复制**调用线程**，其他线程在子进程中不存在；如果某个线程在 fork 瞬间持有锁（logging、连接池、随机数、malloc arena），子进程里的这把锁永远不会释放。`os.register_at_fork(before=..., after_in_parent=..., after_in_child=...)` 在 fork 前后插入回调：`before` 在 fork 前父进程里跑（可用来抢锁/停后台线程），`after_in_parent` 在父进程 fork 返回后跑，`after_in_child` 在子进程里、`fork()` 返回前跑。子进程里只应做 async-signal-safe 的事，Python 回调本身有风险，但用来重置"进程本地状态"是常见做法。

取舍：a) 子进程必须重置：数据库/Redis 连接（句柄共享会导致协议错乱）、线程池/日志锁、随机数状态、PID 缓存、`threading.local`；b) 不要试图在 `after_in_child` 里重建复杂连接池（可能触发 malloc/import 死锁），标记为"懒重建"更稳；c) `before` 里抢到锁不一定安全，其他线程可能继续持有别的锁；最稳的是 fork 前让进程处于"单线程可 fork"状态（preload 只加载代码，不启动线程）；d) Python 3.12 的 `os.fork()` 在有多线程时会发 `DeprecationWarning`，未来版本可能直接报错，生产应优先 `spawn`/`forkserver`；e) `register_at_fork` 是进程级全局注册，无法按 fork 点撤销，测试里要隔离。

实战：事故形态是"preload 模式下主进程初始化了 logging 和 DB 池，worker fork 后继承了被其他线程持有的日志锁，第一次打日志就死锁；在 `after_in_child` 里重置 logging handler 并清空连接池引用后恢复"。下面演示三个回调的执行顺序与子进程状态隔离。

```python
import os

events = []


class Pool:
    def __init__(self):
        self.connections = ["conn-1", "conn-2"]


POOL = Pool()


def before_fork():
    events.append("before")


def after_parent():
    events.append("parent")


def after_child():
    events.append("child")
    POOL.connections.clear()       # 子进程不能复用父进程的连接


os.register_at_fork(
    before=before_fork,
    after_in_parent=after_parent,
    after_in_child=after_child,
)

pid = os.fork()
if pid == 0:
    print("[child] events:", events, "connections:", POOL.connections, flush=True)
    os._exit(0)

os.waitpid(pid, 0)
print("[parent] events:", events, "connections:", POOL.connections)
print("[note] fork 只复制调用线程；其他线程持有的锁在子进程里可能永久锁死")
```

**追问一**：为什么 `after_in_child` 里不能随便打日志？—— 日志 handler 可能持有锁，而 fork 时锁的状态被复制；如果锁被"消失的线程"持有，子进程里 `logging.info` 会永久阻塞。回调里应该只做最小状态重置（把引用置空、把标志位复位），真正的重建延迟到第一次使用。`os.register_at_fork` 的回调本身也在"fork 后、exec 前"的脆弱窗口，不应做 IO。

**追问二**：`multiprocessing` 的 `spawn`/`forkserver` 能完全避免吗？—— `spawn` 不 fork 当前进程，子进程重新 import 模块、重新初始化，天然没有锁继承问题，但启动慢、要求可 pickle；`forkserver` 由一个干净的单线程服务进程 fork，避免多线程 fork 的锁问题，是 Linux 上较稳的折中。代价是全局状态不共享、启动开销增加。新项目优先 `spawn`/`forkserver`，老项目用 `register_at_fork` 兜底。

## 背诵要点
- `fork` 只复制调用线程；其他线程持有的锁在子进程里可能永久锁死。
- `before` → fork → `after_in_parent`/`after_in_child`；子进程重置连接、锁、缓存，重建延迟到首次使用。
- 3.12 多线程 fork 有 DeprecationWarning；优先 `spawn`/`forkserver`。

## 复盘追问
- preload 后 worker 第一次打日志就卡死，怎么解释？（继承的 logging 锁无人释放）
- fork 后数据库连接为什么会串包？（父子共享同一 socket 的文件偏移/协议状态）
