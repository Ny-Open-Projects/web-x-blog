---
title: [Q5551] 线程池复用导致 threading.local 残留污染事故
date: 2026-11-20
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5551 · 线程池复用导致 threading.local 残留污染事故

> 难度:★★★★ | 标签:threading.local, 线程池, contextvars, 事故复盘

**问**：一个内部工具把 `threading.local` 当"请求上下文"用，偶发出现用户 A 看到用户 B 的数据。线程池下 `threading.local` 的生命周期到底是什么？为什么偶发而不是必现？正确选型是什么？

**答**：`threading.local` 的生命周期是**线程**，不是任务。线程池复用线程：任务 1 写入 `tls.user = "user-1"` 后不清理，任务 2 恰好落到同一线程，读到上一单的 user——必现 bug 被"任务分配的随机性"稀释成偶发，且压测里 max_workers 越接近任务数越难复现，是典型的环境敏感竞态。三条修复路线：a) **任务开头显式重置**：每个任务第一行把用到的所有 tls 键清掉，靠纪律，漏一个键就复发；b) **用 `contextvars`**（正解）：`ContextVar` 的隔离单位是执行上下文，`ThreadPoolExecutor` 默认每个任务拷贝提交方的 context，任务内 `set/reset` 天然不跨任务泄漏；c) 结构上消灭"隐式全局"——上下文显式作为参数传。迁移注意：`asyncio` 里 `threading.local` 完全错误（一个线程跑 N 个协程），必须 contextvars；反过来 `contextvars` 在裸线程间不自动传播，跨线程投递要用 `contextvars.copy_context().run()`。这一对工具的分工口诀：**线程池任务用 contextvars，进程级缓存用 threading.local，跨线程外传用 copy_context**。

```python
# file: code/02_并发与网络工程/q5551_tls_pollution.py
import threading
import contextvars
from concurrent.futures import ThreadPoolExecutor

# 1) 事故复现: tls 残留跨任务泄漏
tls = threading.local()
seen = []
def task(i):
    if hasattr(tls, "user"):
        seen.append(("残留", getattr(tls, "user"), "->", i))
    tls.user = f"user-{i}"          # 反例: 任务结束不清理
with ThreadPoolExecutor(max_workers=2) as ex:
    list(ex.map(task, range(6)))
print("线程复用导致 tls 残留:", seen[:3])

# 2) 正解: contextvars, 任务边界天然隔离
cv_user = contextvars.ContextVar("user", default=None)
ok = []
def task2(i):
    token = cv_user.set(f"user-{i}")
    ok.append((i, cv_user.get()))
    cv_user.reset(token)
with ThreadPoolExecutor(max_workers=2) as ex:
    list(ex.map(task2, range(6)))
print("contextvars 各任务互不污染:", ok[:3])

# 3) 跨线程投递上下文: copy_context().run
import time
def worker(cv):
    print("新线程里读上下文:", cv.run(cv_user.get))
ctx = contextvars.copy_context()      # 捕获当前上下文快照
cv_user.set("from-main")
t = threading.Thread(target=worker, args=(ctx,))
t.start(); t.join()
```

**追问**：1) `ContextVar.set` 返回的 Token 为什么必须 `reset`？——不 reset 的话值留在上下文里直到任务结束；在复用上下文的框架（如线程池复用、uvloop 的任务复用场景）里同样会残留，`reset(token)` 才是完整的事务。2) 为什么 set 后必须取 `cv.get()` 而不能缓存 `cv.set` 的值传给函数？——`set` 在协程/线程的当前 Context 里生效，`get` 也在同一 Context 里读，中途被框架切换（await 边界）后读写仍然一致；自己传值会绕过上下文语义，退化成普通变量。3) 日志里带 user id 的请求上下文怎么做？——Filter 从 ContextVar 读值注入 record（或 logging 的 contextvars 支持），替代把 user 塞进 threading.local 的旧写法。

## 背诵要点
- `threading.local` 隔离单位是线程，线程池复用线程 → 上一任务的值残留；必现竞态被调度随机性稀释成偶发。
- 正解 `contextvars`：任务边界天然隔离，配 `token = cv.set()` + `cv.reset(token)` 成对使用。
- 跨线程传上下文用 `contextvars.copy_context().run()`；asyncio 里禁用 threading.local（一线程 N 协程）。

## 复盘追问
- 你们代码里还有几处 threading.local？逐个判断该归 contextvars、显式参数还是真线程级缓存？（提示：grep threading.local，按"值的生命周期"归类）
- "偶发串号"事故怎么定位到线程池残留？复现手法是什么？（提示：把 max_workers 调小+任务里 sleep 抖动放大复用概率，日志记录 threading.get_ident() 对账）
