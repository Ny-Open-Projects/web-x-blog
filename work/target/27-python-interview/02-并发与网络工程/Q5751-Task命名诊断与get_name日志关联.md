---
title: "[Q5751] asyncio Task 命名诊断：name=、get_name 与故障定位的日志关联"
date: 2026-11-24
categories: [Python并发网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5751 · asyncio Task 命名诊断：name=、get_name 与故障定位的日志关联

难度：P5 ｜ 标签：asyncio、create_task、Task name、get_name、set_name、all_tasks、异常诊断、日志关联、task factory

**问**：为什么"任务全靠默认名 Task-N"的服务在故障排查时基本瞎掉——Task 命名（`create_task(name=...)`/`set_name`/`get_name`）怎么接入日志与异常诊断？`asyncio.all_tasks()` 按名过滤能做什么巡检？任务异常的 done 回调里怎么把 name、exception、堆栈串成一条诊断线？与 Q5732 线程命名（thread_name_prefix）、Q2679 Task 工厂的分工边界？

**答**：
结论：默认任务名是 `Task-N`（递增计数，跨进程无规律），它**不携带任何业务身份**——出问题时"Task-7 炸了"不知道对应哪个订单/哪个连接，日志只能靠 traceback 里的协程源码行猜测。Task 命名三件套把"业务身份"挂到运行时对象上：①**创建期命名**——`create_task(coro, name="order-pipeline-1001")`（3.8+），名字建议带业务主键与前缀（`类型-主键`），让 `grep` 日志、metrics 标签、`all_tasks()` 过滤共用同一个键；②**运行期读取**——`task.get_name()` 在 done 回调/异常处理器/巡检脚本里取身份；协程内部用 `asyncio.current_task().get_name()` 把名字打进日志（配合 logging 的 taskname 字段即"每任务一 tag"）；③**阶段改名**——`task.set_name("...:retrying")` 让长生命周期任务的身份随阶段演进（心跳→排空中），改名是**原子字符串替换**不引发任何回调。诊断闭环的标准形态：`add_done_callback` 里统一拿 `task.get_name()` + `task.exception()`（或 `task.cancelled()`）写告警——**收尾纪律（Q1587）与命名纪律在这里合并**：每个 fire-and-forget 任务都挂这个回调，任何异常都能定位到业务实体。巡检形态：`asyncio.all_tasks()` 按名前缀聚合（多少个 order-pipeline 在飞、每个运行多久），泄漏/堆积一眼可见（Q5681 的 all_tasks 差分 + 命名 = 可归因的泄漏画像）。与线程命名的分工：Q5732 的 thread_name_prefix 管的是**线程池**（to_thread/run_in_executor 里的 OS 线程身份），Task 命名管**协程层**——两层命名在"线程池桥接"场景要用同一个业务键（Task 名与线程日志的关联靠 trace_id 而不是 name 直通）；Q2679 的 Task 工厂是**批量定制**机制（subclassing、上下文绑定），命名只是工厂顺手做的事之一。

取舍：a) 名字的成本：name 只是字符串属性，几乎零开销——没有"要不要命名"的问题，只有"命名规范好不好"的问题（无前缀的裸名字过滤不动、纯主键没有类型语义）；b) 唯一性纪律：Task 名**不强制唯一**（同名任务合法），业务键入名时要自己保证（订单号+阶段+序号），巡检逻辑不能假设唯一；c) 与 trace_id 的关系：name 是"任务身份"（一个任务一个），trace_id 是"请求链路"（跨任务/跨进程）——名字不要承载 trace_id（任务里又创建子任务会断链），用 contextvars 传 trace_id（Q387），name 只承载"这个任务是谁"；d) 改名的克制：set_name 用于阶段演进，别在热循环里高频改名（日志系统按名聚合会被改名切割成两条曲线）。

实战：事故形态是"支付网关 night 峰值告警'Task-53 raised ValueError'，on-call 只能从 traceback 反查协程文件行号，定位到业务订单花了 20 分钟——因为任务都是 create_task(coro) 裸创建；且巡检脚本数不出'当前有多少笔清算任务在飞'，只能看 CPU 猜积压"。修复为：所有 create_task 走统一封装（name=f"settle-{order_id}-{seq}" 强制命名 + done 回统一告警），巡检脚本 `all_tasks()` 按前缀聚合输出"类型/数量/最长运行时长"，报警直接带任务名。下面实测命名、过滤、done 回调诊断与动态改名。

```python
# asyncio Task 命名诊断: name= / set_name / get_name 与故障定位
import asyncio
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("q5751")

async def order_pipeline(order_id: int):
    await asyncio.sleep(0.02)
    raise ValueError(f"order {order_id} 转账失败")

async def main():
    print("[1] 未命名任务的默认 name 是 Task-N (无业务含义)")
    t_default = asyncio.create_task(asyncio.sleep(0.01))
    print("    default name:", t_default.get_name())

    print("[2] create_task(name=...) 命名 + all_tasks 按名过滤")
    t1 = asyncio.create_task(order_pipeline(1001), name="order-pipeline-1001")
    t2 = asyncio.create_task(order_pipeline(1002), name="order-pipeline-1002")
    heartbeat = asyncio.create_task(asyncio.sleep(3600), name="heartbeat")
    named = [t.get_name() for t in asyncio.all_tasks() if t.get_name().startswith("order")]
    print("    按前缀过滤:", sorted(named))

    print("[3] done 回调关联任务名: 诊断入口统一拿 get_name() + exception()")
    caught = []
    def on_done(task: asyncio.Task) -> None:
        exc = task.exception() if not task.cancelled() else None
        caught.append((task.get_name(), repr(exc)))
    t1.add_done_callback(on_done)
    t2.add_done_callback(on_done)
    await asyncio.gather(t1, t2, return_exceptions=True)
    print("    回调捕获:", sorted(caught))

    print("[4] set_name 动态改名: 任务身份随业务阶段演进")
    hb_probe = heartbeat
    hb_probe.set_name("heartbeat:draining")
    print("    改名后:", hb_probe.get_name())

    print("[5] 当前任务名: current_task().get_name() 打进日志")
    async def tagged(tag: str) -> None:
        log.info("[%s] task=%s", tag, asyncio.current_task().get_name())
    await asyncio.gather(tagged("a"), tagged("b"))
    for t in (t1, t2, heartbeat):
        t.cancel()

asyncio.run(main())
print("[rule ] 长生命周期任务一律 name= 命名; done 回调读 get_name()+exception() 关联业务; 阶段演进用 set_name")
```

**追问一**：Task 名与 contextvars 的 trace_id 在"诊断标签体系"里怎么分工？为什么 trace_id 不能塞进 Task 名？—— 分工：Task 名回答"**这个任务是谁**"（创建时的静态身份，主键+类型+序号），trace_id 回答"**这条链路经过哪里**"（跨任务、跨线程池、跨服务的动态传播链）。trace_id 不能进 Task 名的三个原因：①**传播断裂**——任务内部再 create_task 子任务时，子任务名不会自动带父名（name= 是显式参数），trace 链断；而 contextvars 的 Context 是**创建时快照继承**（子任务自动携带，Q387），传播零成本；②**多链路混淆**——一个任务可能处理多个逻辑链路（聚合任务），名字是单值容器塞不下；③**生命周期错位**——改名阶段演进（[4]）与 trace 常量是两个维度的变化，混在一个字符串里日志聚合两头受损。落地标签体系：Task name 承载身份进日志字段 `task_name`，contextvars 承载 trace_id 进 `trace_id`，metrics 标签用 task name 前缀聚合（注意基数控制——前缀聚合而非全名聚合，订单号级别的标签会把 Prometheus 打爆，只对错误率这类低基数指标用全名）。create_task 封装层同时做三件事：强制 name、挂 done 回调、拷贝 context（create_task 默认继承当前 context，封装里显式 ensure_future 语义一致）。

**追问二**：怎么写一个"任务巡检器"——定期输出按名前缀聚合的任务画像（数量/最长运行/堆积告警）？实现要点与误报治理？—— 骨架：①**采集**——`asyncio.all_tasks()` 返回当前仍在运行的任务集合（含当前巡检任务自己，要排除），每任务取 `get_name()`、`get_coro()` 的起始行、`get_stack()` 深度；②**聚合**——按 name 的类型前缀（约定取 `-` 前第一段或显式 type 字段）分组：count、max_age（任务创建时间怎么拿？Task 没有暴露创建时间戳——用自定义封装在创建时记录 `time.monotonic()` 存进 task 属性 `task.start_ts = ...`，或 Task 子类）；③**告警规则**——某前缀 count 超阈值（任务堆积）、max_age 超 SLA（任务卡死）、连续 N 轮出现"同一主键的任务"（同一订单被重复派发，命名唯一性纪律的副作用检测）；④**输出**——日志行（结构化 JSON）+ 可选暴露到 metrics。误报治理：巡检器自己要被排除（current_task 过滤）、done 但未回收的任务会短暂出现在 all_tasks（加状态过滤 `not t.done()`）、await 挂起在 sleep 的健康任务别误判卡死（卡死判定要"超 SLA 的运行时长"而不是"处于 SUSPENDED"——协程本来就是挂起态）。巡检器的安全红线：巡检只读不杀（发现堆积告警给人处理，自动 cancel 任务是另一套带灰度的运维动作，与 Q5603 的速率治理联动）。

## 背诵要点
- 默认名 Task-N 无业务含义；三件套：create_task(name=) 创建期命名、get_name()/current_task().get_name() 诊断读取、set_name() 阶段演进改名。
- 诊断闭环：每个 fire-and-forget 任务挂 done 回调统一读 get_name()+exception()；all_tasks() 按名前缀聚合出任务画像（数量/最长运行/堆积）。
- 分工：Task name=任务身份（静态主键），trace_id 走 contextvars（创建时快照继承、跨层传播）——trace_id 不进 Task 名；与 Q5732 线程命名分层。

## 复盘追问
- "Task-53 炸了"为什么难排查、修复的封装层要做什么？（默认名无业务身份；统一 create_task 封装强制命名+done 回调+巡检按前缀聚合）
- Task 名与 trace_id 为什么不能合并、各自怎么传播？（name 单值静态、子任务不自动继承；contextvars 快照继承自动传播，跨任务/线程不断链）
