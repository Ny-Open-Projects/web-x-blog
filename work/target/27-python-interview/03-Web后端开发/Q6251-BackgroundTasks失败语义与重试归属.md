---
title: "[Q6251] BackgroundTasks 的失败语义：先发 200 再执行，异常由谁接住、重试由谁负责"
date: 2026-11-25
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6251 · BackgroundTasks 的失败语义：先发 200 再执行，异常由谁接住、重试由谁负责

难度：P6 ｜ 标签：FastAPI、Starlette、BackgroundTasks、响应后执行、异常吞噬、重试、消息队列、幂等

基线：库知识卡，代码用标准库模拟 BackgroundTasks 的"响应后执行"顺序与异常传播。

**问**：一个下单接口把"发确认邮件、写审计日志、同步库存"都塞进了 `BackgroundTasks`，接口 P99 很好看，但月底对账发现部分审计日志缺失、库存偶发不同步；查日志只看到 `Exception in ASGI application`，客户端却全是 200。BackgroundTasks 到底在什么时候执行？任务抛异常时响应会变吗、谁来重试？哪些任务绝对不能放在这里？

**答**：

- **结论**：Starlette 的 `BackgroundTasks` 挂在 `Response.background` 上，执行顺序是**先把响应完整发给客户端（包括 body 刷出），再 `await background()`**。所以：①任务执行时状态码已经确定并发出，任务失败**不会**把 200 改成 500；②任务抛出的异常会向上冒泡到 ASGI server（uvicorn 打 "Exception in ASGI application"），但连接上的响应已经完成，客户端无感；③没有重试、没有持久化、没有跨进程投递——任务只存在于当前 worker 的内存里，进程崩溃/重启/被 SIGKILL 就丢；④任务是**串行**执行的（一个 `BackgroundTasks` 实例按 add 顺序逐个 await），一个慢任务会拖住同一个响应的后续任务，也会拖住 worker 的 graceful shutdown。它适合"可丢、幂等、短小"的收尾工作（访问日志、缓存预热、指标上报），不适合"必须成功"的业务动作（扣库存、发钱、发邮件回执）。

- **取舍**：a) 放在 BackgroundTasks：延迟敏感但可容忍丢失的副作用，且执行时间要短（毫秒级），不能让 worker 在响应后还挂着长任务；b) 放消息队列：需要重试、持久化、削峰、跨服务解耦的动作；代价是引入 broker、消费者、幂等键、死信队列，链路更长；c) 折中：先写"本地 outbox 表"（与业务同事务），再由后台消费者投递，保证"业务成功则消息最终一定发出"；d) 不要让 BackgroundTasks 承担"顺序敏感"的多步业务：它没有事务、没有回滚，前一个任务成功、后一个失败会留下半完成状态。

- **实战**：事故形态是"审计日志偶发缺失"——审计任务依赖一个下游 HTTP 接口，下游抖动时任务抛异常，异常被 server 记录但没人告警；更糟的是任务在响应后执行，K8s 滚动发布时 worker 收到 SIGTERM，正在跑的任务被中断，日志既没写成功也没进死信。修复：①审计改为"写本地 outbox 表 + 独立消费者"，与订单同事务；②必须留在 BackgroundTasks 的任务加"幂等键 + 失败落盘重试"；③监控不再只看 HTTP 5xx，而是采集 "background task failed" 日志并告警；④优雅停机时等待 background 完成（或明确设置超时），不要把"响应已发"误当成"任务已完成"。

```python
# 模拟 Starlette BackgroundTasks: 先发响应, 再串行执行; 异常冒泡到 server 而非客户端
class BackgroundTasks:
    def __init__(self):
        self._tasks = []

    def add_task(self, fn, *args, **kwargs):
        self._tasks.append((fn, args, kwargs))

    async def __call__(self):
        for fn, args, kwargs in self._tasks:
            await fn(*args, **kwargs)      # 串行; 异常直接向上抛

class Response:
    def __init__(self, status, body, background=None):
        self.status = status
        self.body = body
        self.background = background

    async def send(self, client):
        client.append(("status", self.status))
        client.append(("body", self.body))  # 响应先完成
        if self.background is not None:
            await self.background()         # 之后才跑任务

async def main():
    client = []
    attempts = {"audit": 0}

    async def send_audit(order_id):
        attempts["audit"] += 1
        raise RuntimeError("downstream audit service unavailable")

    async def warm_cache(order_id):
        client.append(("cache", order_id))

    tasks = BackgroundTasks()
    tasks.add_task(send_audit, "A100")
    tasks.add_task(warm_cache, "A100")

    resp = Response(200, {"ok": True}, background=tasks)
    server_error = None
    try:
        await resp.send(client)
    except RuntimeError as e:
        server_error = e

    print("→ 客户端看到的事件:", client)
    print("→ 服务端捕获的异常:", server_error)
    print("→ 审计任务尝试次数:", attempts["audit"])

    assert client[0] == ("status", 200)          # 状态码已发出
    assert ("body", {"ok": True}) in client      # body 已发出
    assert server_error is not None              # 异常冒泡到 server
    assert attempts["audit"] == 1                # 没有自动重试
    assert ("cache", "A100") not in client       # 前一个任务抛错, 后续任务没跑

    # 幂等键 + 重试要自己做: 这里用"最大尝试次数"演示消费者语义
    delivered = []
    async def consume_with_retry(key, max_try=3):
        for i in range(1, max_try + 1):
            try:
                if i < 3:
                    raise TimeoutError("audit timeout")
                delivered.append((key, i))
                return i
            except TimeoutError:
                continue
        raise RuntimeError("dead letter")

    n = await consume_with_retry("A100")
    print("→ 队列消费者重试后成功:", delivered, "尝试次数:", n)
    assert n == 3 and delivered == [("A100", 3)]

import asyncio
asyncio.run(main())
```

**追问一**：BackgroundTasks 的异常为什么不会变成 500？如果任务在响应发送**之前**就失败呢？—— 顺序决定语义：`Response.__call__` 先 `await send(...)` 把 `http.response.start` 和 `body` 发完，再 `await self.background()`；异常发生时状态行和 body 都已经在 socket 上，HTTP 协议不允许"撤回"，所以只能记录。反过来说，如果任务在响应发送前执行（比如依赖里做副作用），异常就会进入正常的异常处理链，变成 500——这也是为什么"把业务动作放在依赖的 `yield` 前"和"放在 BackgroundTasks"是完全不同的可靠性语义。另一个细节：`BackgroundTasks` 是串行的，第一个任务抛错会跳过后续任务；需要"互不影响"就得每个任务自己 try/except，或者拆成多个独立的后台任务。

**追问二**：为什么"发邮件"通常不应该放 BackgroundTasks，而"写访问日志"可以？—— 判据是**丢失的代价**与**重试的必要性**：发邮件是用户可感知的业务承诺，丢了要补偿、要重试、要审计，必须有持久化（outbox/队列）和幂等键；访问日志丢了通常可接受（或者有上游 LB 日志兜底），且写入是幂等的（同一条日志重复写最多多一行）。此外邮件发送可能耗时数秒，放在 BackgroundTasks 会让 worker 在响应后继续占用事件循环（同步 SMTP 还会阻塞），滚动发布时容易被 SIGKILL 打断。结论：BackgroundTasks 是"进程内的 best-effort 收尾"，不是"可靠任务队列"；把可靠性需求写进选型，而不是等对账时才发现。

## 背诵要点

- BackgroundTasks 在响应 body 发完之后串行执行；任务异常只冒泡到 ASGI server，客户端仍是 200，没有重试/持久化。
- 只适合可丢、幂等、毫秒级的收尾；必须成功的动作走消息队列或本地 outbox + 消费者。
- 第一个任务抛错会跳过后续任务；进程退出/滚动发布会丢任务，监控要单独采集 background 失败日志。

## 复盘追问

- 为什么客户端全是 200，审计日志却缺了？（响应先发，任务后跑；异常只到 server 日志，状态码无法回改）
- 下单后的"扣库存/发邮件"应该放哪？（可靠动作走 outbox/队列 + 幂等键；BackgroundTasks 只做可丢的收尾）
