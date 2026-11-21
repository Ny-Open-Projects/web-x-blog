---
title: [Q5051] 解释器关闭阶段 __del__ 与 atexit 事故复盘
date: 2026-11-20
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5051 · 解释器关闭阶段 `__del__` 与 atexit 的事故复盘

> 难度:★★★★ | 标签:shutdown, atexit, __del__, weakref.finalize, 事故复盘

**问**：一次退出挂死事故：服务收到 SIGTERM 后，日志里出现一堆 `Exception ignored in: <function Conn.__del__>`，有时还卡住不退出。解释器关闭阶段发生了什么？为什么 `__del__` 在关闭时不可靠？生产代码的资源清理应该怎么写？

**答**：正常退出时 CPython 按顺序做三件事：主代码跑完/收到退出 → 调用 atexit 注册的钩子（LIFO，后注册先执行）→ 最后对残余对象做一次"清场"式回收，此时才触发没被回收对象的 `__del__`。事故根因是 `__del__` 依赖了模块级全局（连接池、logger、线程锁）：解释器关闭时模块全局正在被逐个置 `None`/清空，`__del__` 一执行就撞上 `AttributeError: 'NoneType'`，CPython 只能打印 `Exception ignored`；如果 `__del__` 还试图拿一把已被销毁的锁或 join 一个 daemon 线程，进程就挂死。三条铁律：a) **清理逻辑写进显式的生命周期钩子**（框架 lifespan/上下文管理器/finally），不要指望 `__del__`；b) 必须"兜底"清理时用 `weakref.finalize` 而不是 `__del__`——它持有独立的回调与参数，注册为 atexit 时不受模块全局清理影响，还能 `atexit=False` 禁掉关闭期行为；c) atexit 钩子要幂等且不阻塞（不 join 长任务），优雅停机的 drain 逻辑放在信号处理处而不是 atexit 里。另外：解释器关闭时 daemon 线程是被硬杀的，它们持有的队列（如 logging 的 QueueListener）来不及 flush，日志丢失就是这么来的。

```python
# file: code/01_语言核心与底层/q5051_shutdown_del.py
import atexit, gc, weakref

ORDER = []

class Conn:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        # 关闭期若引用了模块全局(pool/logger), 此处会 Exception ignored
        ORDER.append(("del", self.name))

def shutdown_hook():
    ORDER.append("atexit-hook")   # atexit 先于解释器清场执行

atexit.register(shutdown_hook)
c = Conn("db")
del c                  # 运行期立即触发 __del__, 此时一切正常
gc.collect()
ORDER.append("main-end")
print("运行期 del 在 atexit 之前:", ORDER)

# 兜底清理的正解: weakref.finalize, 回调自带参数, 不依赖模块全局
r = weakref.finalize(Conn("x"), lambda n: print("finalize 兜底释放:", n), "x")
r.atexit = True        # 进程退出时自动执行(默认即 True)
print("finalize alive:", r.alive)

# 生产铁律: 关键资源显式收尾, finalize 只做防漏兜底
# with ctx / lifespan -> finally: conn.close(); finalize 兜底防漏
```

**追问**：1) atexit 注册两个钩子，执行顺序是什么？——LIFO（后注册先执行），与栈式清理语义一致；所以"后申请的资源先释放"天然成立，依赖关系要按注册顺序倒排。2) `os._exit(0)` 与 `sys.exit(0)` 的区别对清理的影响？——`sys.exit` 走正常退出流程（finally/atexit/finalize 都会跑），`os._exit` 直接内核级终止，什么都不跑；fork 出的子进程必须用 `os._exit` 避免重复执行父进程的清理钩子。3) 为什么关闭期 daemon 线程会丢日志？——daemon 线程随解释器硬杀，QueueListener 没机会 stop；解法是把 QueueListener.stop 注册进生命周期钩子，非 daemon 运行。

## 背诵要点
- 关闭顺序：atexit 钩子（LIFO）→ 解释器清场回收触发 `__del__`；清场期模块全局已置 None，`__del__` 引用全局必炸。
- 兜底清理用 `weakref.finalize`（自带参数不依赖全局，atexit 可控）；关键资源必须显式 close/lifespan 收尾。
- `sys.exit` 走完整清理，`os._exit` 全部跳过（fork 子进程用它防钩子重复执行）；daemon 线程关闭期被硬杀会丢 flush。

## 复盘追问
- 你们服务的优雅停机里，哪些清理放在信号处理、哪些放在 atexit、哪些依赖 `__del__`？为什么这样分？（提示：信号处理做 drain，生命周期钩子关资源，finalize 只兜底）
- 如果 `__del__` 里的异常只打印不中断，你怎么在生产上发现它？（提示：`Exception ignored` 进 stderr，把 stderr 收进日志管道并按关键字告警）
