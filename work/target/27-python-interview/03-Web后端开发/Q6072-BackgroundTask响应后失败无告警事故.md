---
title: [Q6072] BackgroundTask 响应后失败无告警的事故复盘
date: 2026-11-21
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6072 · BackgroundTask 响应后失败无告警的事故复盘

> 难度:★★★★ | 标签:事故复盘, Starlette, BackgroundTasks, 可靠性

**问**：订单接口把"发通知、写统计"塞进 FastAPI 的 `BackgroundTasks`，响应 200 返回后任务悄悄失败，用户没收到通知却无任何告警，持续一周。BackgroundTasks 的执行时机与异常去向是什么？它和"真任务队列"（Celery/RQ/arq）的可靠性差距在哪几层？什么边界内可以用 BackgroundTasks、什么边界必须换队列？

**答**：结论：Starlette 的 `BackgroundTasks` 是**响应完成后的进程内同步/异步直调**——`Response.__call__` 发完 body 后在同一个 ASGI 调用里顺序执行 `task()`；异常若无人捕获，会沿 ASGI 协议抛给服务器，uvicorn 会记一条 error 日志并关闭该连接，但**请求已经 200 成功、指标上是一次正常请求**——没有状态码可告警、没有重试、没有持久化，进程重启即丢失。可靠性差距四层：a) **持久化**：队列表/消息在 broker 或 DB 里，进程崩了任务还在；BackgroundTasks 只存在于当前协程栈，崩即失；b) **重试**：队列有 ack/重试/死信（DLQ）；BackgroundTask 异常即终局；c) **可观测**：队列任务有状态机（pending/done/failed）可查可告警；BackgroundTask 只有日志；d) **隔离**：任务失败不影响 worker 主流程（连接池、内存、重启独立）；BackgroundTask 与请求共享进程资源，任务重（大对象、慢 IO）会拖累整个服务。边界划分（工程口径）：适合 BackgroundTasks 的只有"**失败可容忍 + 耗时 < 1s + 与响应同生命周期**"的收尾动作：清理临时文件、打点日志、审计埋点（且打点失败无业务后果）；一旦任务"有业务后果"（通知、计费、状态推进）或耗时不可控，必须出队列（arq/Celery/自建 outbox，Q6049 双写与 Q6041 的连接池联动）。实战补救：把现有 BackgroundTasks 盘点分类，"有业务后果"的迁队列，迁不了的至少包 try/except + 告警埋点 + 落本地 outbox 表。

```python
# file: code/03-Web后端开发/q6072_background_task.py
import asyncio, time, sys

# 1) Starlette BackgroundTasks 的执行时机: 响应体发完后、同一 ASGI 调用内
async def risky_notify():
    raise RuntimeError("下游通知服务超时")     # 事故: 响应已 200, 这里才炸

class BackgroundTasks:
    def __init__(self): self.tasks = []
    def add_task(self, fn, *a): self.tasks.append((fn, a))

class FakeResponse:
    def __init__(self, bg): self.bg = bg
    async def __call__(self, send):
        await send({"type": "body"})            # 模拟发完响应体(此刻已 200)
        for fn, a in self.bg.tasks:
            await fn(*a)                        # 同进程直调, 异常无人兜底

async def request_flow():
    bg = BackgroundTasks(); bg.add_task(risky_notify)
    resp = FakeResponse(bg)
    status = "200 OK"                           # 接口层视角: 请求成功
    try:
        await resp(send=lambda m: asyncio.sleep(0))
    except RuntimeError as e:
        print(f"接口已返回 {status}, 但后台任务炸了: {e}")
        print("uvicorn 只会记一条 error 日志+关连接, 无状态码可告警、无重试、无持久化")

asyncio.run(request_flow())

# 2) 正确形态: 本地 outbox 表 + 独立 worker(事务性投递)
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE outbox(id INTEGER PRIMARY KEY, topic TEXT, payload TEXT, status TEXT DEFAULT 'pending', tries INT DEFAULT 0)")
db.execute("INSERT INTO outbox(topic, payload) VALUES('notify', 'order-1')")

async def worker():
    while True:
        row = db.execute("SELECT id, payload, tries FROM outbox WHERE status='pending' ORDER BY id LIMIT 1").fetchone()
        if not row: return
        id_, payload, tries = row
        try:
            raise RuntimeError("模拟首试失败" if tries == 0 else None) if tries == 0 else None
        except RuntimeError as e:
            db.execute("UPDATE outbox SET tries=tries+1, status=? WHERE id=?",
                       ("failed" if tries >= 1 else "pending", id_))
            print(f"outbox 任务 {id_} 失败重试(tries={tries+1}): {e}")
        else:
            db.execute("UPDATE outbox SET status='done' WHERE id=?", (id_,))
            print(f"outbox 任务 {id_} 成功: {payload}")
        await asyncio.sleep(0)

asyncio.run(worker())

# 3) 边界判定(输出): 可容忍+<1s+同生命周期 -> BackgroundTasks; 有业务后果 -> 队列
print("边界: 清理临时文件/打点=可用 BackgroundTasks; 通知/计费/状态推进=必须 outbox/Celery/arq")
print("python:", sys.version.split()[0])
```

**追问**：1) 为什么 BackgroundTasks 不在响应前执行？——HTTP 语义：响应先到客户端（体验要求），收尾工作不阻塞响应；代价是任务失败时响应已不可更改，也无法把任务失败反馈给调用方——所以需要"业务后果"的任务根本不该走这条路，这是设计使然而不是 bug。2) 事务性 outbox 的关键点？——业务写库与 outbox 插入在**同一事务**（sqlite 演示中简化了），保证"业务成功⇒任务必达"；worker 轮询/监听 outbox 投递，重试次数与 DLQ 收口（Q6049 双写不一致的失败矩阵同一套思路）；注意 worker 幂等（同一任务可能投递多次）。3) FastAPI 里怎么让"必达任务"代码看起来仍然干净？——依赖注入 outbox 写入器：`Depends(get_outbox)`，接口只往 outbox 塞记录，投递交给独立进程/容器（与 API 服务重启隔离），监控指标 = outbox 表 pending 积压量与最老任务年龄（两指标告警，见 Q6073 积压容量账）。

## 背诵要点
- BackgroundTasks 在响应体发完后同进程直调：异常无状态码可告警、无重试、无持久化，进程重启即丢。
- 与真队列的差距四层：持久化、重试/DLQ、状态机可观测、资源隔离；"失败可容忍+<1s+同生命周期"才可用 BackgroundTasks。
- 补救路径：盘点分类 → 有业务后果的迁 outbox/Celery/arq；outbox 与业务同事务写入 + worker 幂等投递 + 积压量/最老任务年龄双告警。

## 复盘追问
- 你们接口里还有多少"响应后悄悄执行"的逻辑？当时怎么发现通知丢失持续一周的？（提示：从下游对账单反推，再倒查 BackgroundTasks 清单；把"每请求后台任务数"与"任务失败计数"做成指标）
- 如果通知必须 5 秒内必达，outbox 轮询间隔与 worker 池怎么定？（提示：轮询 ≤1s 或 DB LISTEN/NOTIFY，worker 按峰值 TPS 定，积压告警阈值=2×正常处理时间，联动 Q6073）
