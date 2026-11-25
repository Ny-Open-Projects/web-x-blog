---
title: "[Q5253] inspect.getgeneratorstate：生成器/协程状态机的运行时观测"
date: 2026-11-24
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5253 · inspect.getgeneratorstate：生成器/协程状态机的运行时观测

难度：P6 ｜ 标签：inspect、getgeneratorstate、生成器状态机、GEN_CREATED、GEN_SUSPENDED、GEN_CLOSED、gi_frame、生命周期断言

**问**：生成器/协程的运行时状态机有哪几个状态、分别由什么操作触发迁移？为什么 GEN_CREATED 状态不能直接 `send("boot")`？GEN_CLOSED 之后生成器对象还剩什么（gi_frame 为什么变 None）？`inspect.getgeneratorstate` 在工程上有什么用——它与 Q431/Q432 讲的 send/throw/close 操作语义怎么配合？

**答**：
结论：生成器/协程是一台**显式状态机**，`inspect.getgeneratorstate` 是它的官方观测接口，四个状态与迁移路径：**GEN_CREATED**（刚创建、函数体一行未执行）→ 首次 `next()`/`send(None)` 预激进入 **GEN_SUSPENDED**（挂起在某个 yield/await 处，这是主态，几乎所有生命周期都停留在此）→ 被驱动执行中是 **GEN_RUNNING**（只能在生成器**内部**观测到自己——外部代码在调用 next/send 期间，观测点只在生成器体内）→ 终态 **GEN_CLOSED**（三种路径：函数体正常耗尽抛 StopIteration、显式 `close()`、`throw()` 注入异常未被内部捕获）。GEN_CREATED 不能直接 `send("boot")` 的原因：send 的值要"递给 yield 表达式的求值结果"，而 CREATED 状态**还没有执行到任何 yield**——没有等待取值的位置，CPython 直接 `TypeError: can't send non-None value to a just-started generator`，必须先 next/send(None) 预激（Q2075 预激模式的问题根源）。GEN_CLOSED 后生成器对象本身仍可持有（调用 getgeneratorstate 返回 CLOSED、get_name 等元信息可读），但 **gi_frame 置 None**——挂起帧被释放（Q554 讲过帧是生成器惰性内存的本体，帧释放即恢复内存），此时再 next/send 会抛 StopIteration。工程用途三个：①**生命周期断言**——测试里断言"异常路径后生成器应 CLOSED、资源生成器必须被关闭"，比 try/finally 的人肉纪律可靠；②**诊断悬挂泄漏**——批量巡检 `all_tasks()`/生成器池里的 SUSPENDED 成员，长期 SUSPENDED 且不在等待列表的就是泄漏候选（与 Q5681 的 Task 泄漏差分同思路）；③**防误用护栏**——复用池/调度器在驱动前检查状态，CREATED 先预激、CLOSED 拒绝投递，把状态机的非法迁移在入口拦住。

取舍：a) 观测粒度：getgeneratorstate 只回答四态粗粒度；要知道"挂在哪个 yield"得看 `gi_frame.f_lineno`（帧还在时才可读，CLOSED 后 None）——诊断信息取帧要在 SUSPENDED 时抓；b) 协程同源：`getcoroutinestate` 是独立函数（原生协程不走 inspect 的 generator 接口），状态名不同（CORO_CREATED/SUSPENDED/CLOSED），写通用工具要双接口适配；c) RUNNING 的观测限制：外部永远看不到 RUNNING（观测代码与执行互斥），能看到的只有 SUSPENDED/CLOSED——设计健康检查时不要试图从外部轮询"是否运行中"；d) 与 yield 的关系：一次 `next()` 内生成器从 SUSPENDED→RUNNING→(yield)→SUSPENDED，状态的连续切换是同步的，多线程里两个线程同时驱动同一个生成器会炸 `ValueError: generator already executing`（状态机没有并发保护，Q596 协程并发安全边界的底层原因）。

实战：事故形态是"自研流水线用生成器做任务分片，异常路径里生成器没 close，池子里累积长期 SUSPENDED 的生成器（各挂着一帧局部变量，Q554 的内存账），进程 RSS 缓慢上涨；排查时靠 `inspect.getgeneratorstate` + `gi_frame` 抓快照，把所有 SUSPENDED 生成器的 frame.f_lineno 聚合分布，定位到卡在某个 yield 的分支"。修复为：流水线收口处 finally 强制 close + 周期性状态巡检（SUSPENDED 超时告警）+ 生命周期断言进单测。下面实测四态迁移、预激契约与 CLOSED 后的帧释放。

```python
# inspect.getgeneratorstate: 生成器/协程状态机观测
import inspect

def worker():
    # 全局 g 引用自己 (先赋值 g 再启动生成器)
    inside = inspect.getgeneratorstate(g)   # 运行中观测自己: RUNNING
    yield ("step1", inside)
    yield ("step2", None)

print("[1] 创建未启动: GEN_CREATED, 不能直接 send 非None值")
g = worker()
print("    state =", inspect.getgeneratorstate(g))
try:
    g.send("boot")
except TypeError as e:
    print("    send(非None) -> TypeError:", e)

print("[2] next 预激后: GEN_SUSPENDED (挂起在 yield 处)")
name, inside = next(g)
print("    first =", name, "| 外部观测 state =", inspect.getgeneratorstate(g))

print("[3] 生成器运行中观测自己: GEN_RUNNING")
print("    生成器内部看到的自己:", inside)

print("[4] 正常耗尽后: GEN_CLOSED, gi_frame 变 None")
next(g)
try:
    next(g)
except StopIteration:
    print("    StopIteration 正常结束")
print("    state =", inspect.getgeneratorstate(g), "| gi_frame =", g.gi_frame)

print("[5] close 提前关闭: 也进 GEN_CLOSED")
g2 = worker()
next(g2)
g2.close()
print("    state =", inspect.getgeneratorstate(g2), "| gi_frame =", g2.gi_frame)

print("[6] throw 注入后未捕获: 生成器关闭")
g3 = worker()
next(g3)
try:
    g3.throw(ValueError("inject"))
except ValueError:
    print("    异常从生成器传出")
print("    state =", inspect.getgeneratorstate(g3))
print("[rule ] CREATED 不能 send 非None; SUSPENDED 是主态; RUNNING 内部观测; CLOSED 后 frame=None")
```

**追问一**：GEN_SUSPENDED 与"挂起在哪个 yield"怎么同时观测？这种帧级信息在诊断里怎么用、有什么隐私/安全边界？—— 状态 + 行号组合观测：`state == GEN_SUSPENDED` 且 `g.gi_frame` 非 None 时，`g.gi_frame.f_lineno` 给出挂起处的源码行号、`g.gi_frame.f_locals` 给出局部变量快照——这是"生成器卡在哪一步"的直接证据，流水线卡死诊断里比日志更快（日志需要埋点，帧快照是零侵入的）。用法纪律：①**抓取时机**——必须在 SUSPENDED 时抓，CLOSED 后 frame 为 None，RUNNING 时外部不可达；②**快照要拷贝**——`f_locals` 返回的是实时视图（引用），转 dict 拷贝后再落日志；③**隐私边界**——f_locals 会暴露业务敏感数据（token、用户记录），巡检日志要做字段白名单/脱敏（与 Q1901 日志脱敏同纪律）；④**生命周期**——持有 frame 引用会阻止生成器内存释放（Q5052 traceback 持有 frame 泄漏同机制），快照用完即弃。工程形态：健康巡检只取 f_lineno 聚合分布（哪个 yield 卡了 N 个），f_locals 只在人工排查时按需抓取并打标。

**追问二**：为什么标准库要把 getgeneratorstate 和 getcoroutinestate 做成两个函数？写一个通用的"异步生命周期观测"工具需要注意什么？—— 分裂的历史原因：生成器（PEP 342）与原生协程（PEP 492）是两个独立类型，协程刻意不支持 iter/next 协议（防止被同步 for 循环误驱动），inspect 也就提供了平行接口（getcoroutinestate/getcoroutineframe）。通用工具的适配点：①**类型分派**——`inspect.isgenerator(obj)` vs `inspect.iscoroutine(obj)`，分别取 state；async def 生成的协程对象与 types.coroutine 装饰的生成器协程（Q439 的兼容层）状态语义一致但接口不同；②**状态名映射**——GEN_* 与 CORO_* 的 CREATED/SUSPENDED/CLOSED 三态对齐，RUNNING 都只在内部可见；③**Task 层要再包一层**——asyncio Task 不暴露 generator 接口，用 `task.get_coro()` 拿底层协程再观测，但 Task 的 pending/done 状态与协程状态是两层状态机（Task cancel 后协程抛 CancelledError 再 CLOSED，Q5629 的取消时序），观测工具要区分"Task 状态"与"底层协程状态"；④**生产建议**——健康巡检面向 Task 层（all_tasks + done 回调，Q1587），帧级观测只在事故排查时用，避免常驻巡检持有 frame 的内存副作用。

## 背诵要点
- 四态：GEN_CREATED（未预激）→ GEN_SUSPENDED（主态）→ GEN_RUNNING（仅内部可见）→ GEN_CLOSED（耗尽/close/throw 未捕获三路径）；CLOSED 后 gi_frame=None。
- GEN_CREATED 下 `send(非None)` 直接 TypeError（没有挂起的 yield 接值）——必须先预激；CLOSED 后再驱动抛 StopIteration。
- 工程用途：生命周期断言、SUSPENDED 泄漏巡检（frame.f_lineno 定位卡点）、复用池状态护栏；协程用 getcoroutinestate 平行接口，Task 是另一层状态机。

## 复盘追问
- 为什么 CREATED 状态 send 值会 TypeError？预激的本质是什么？（send 值要交给挂起的 yield 表达式，CREATED 没执行到任何 yield；预激 = next/send(None) 推进到第一个挂起点）
- 怎么诊断"流水线里大量生成器卡住"？（getgeneratorstate 巡检 SUSPENDED + gi_frame.f_lineno 聚合分布定位卡住的 yield；快照即取即弃防 frame 持有泄漏）
