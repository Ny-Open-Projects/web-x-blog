---
title: [Q5510] gRPC/protobuf 流式调用在 asyncio 下的取消传播
date: 2026-11-18
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5510 · gRPC/protobuf 流式调用在 asyncio 下的取消传播

> 难度:★★★ | 标签:gRPC, asyncio, 取消传播

**问**：客户端断开连接后，gRPC 服务端的流式 handler 还在跑——取消是怎么传播的？`grpc.aio` 服务端在客户端 cancel 后 handler 里会看到什么？timeout 在 gRPC 里怎么跨服务传递（deadline propagation）？半途取消的计费/副作用一致性怎么处理？

**答**：结论：gRPC 的取消是**协议级**的：客户端取消调用会发 HTTP/2 RST_STREAM（或 CANCEL 帧），`grpc.aio` 服务端把「流被对端终止」转成 handler 内 await 点抛 `asyncio.CancelledError`——前提是 handler 是真异步（每个 await 都可能被打断），纯 CPU 循环不会被打断，取消只在下一个 await 生效。三件套要点：1) **deadline propagation**：deadline 编在初始 metadata（`grpc-timeout` header），下游调用自动继承剩余预算——上游剩 2s，下游调用自动只给 2s，这是 gRPC 相对裸 HTTP 的最大优势；Python 侧 `call.timeout(x)` 设的是本次调用绝对值，链式传递靠自动继承。2) **服务端清理**：handler 里 try/finally 兜资源，`finally` 里不能做慢操作（取消路径上也占 worker）；需要「客户端走后也要算完」的场景（如批量导出），handler 应把任务转交后台队列再返回，而不是硬扛取消。3) **副作用一致性**：流式调用半途取消 = 客户端看到 CANCELLED 状态，但服务端已完成的部分副作用（已写入 DB、已扣额度）不会自动回滚——要在业务层用幂等键/事务边界兜，gRPC 只保证「通知到位」不保证「结算一致」。版本基线：grpcio==1.60+/grpcio-tools，`grpc.aio` 自 1.32 稳定；纯 asyncio 栈（uvloop + grpc.aio）注意 aio server 与 asyncio.run 的事件循环生命周期配合（`server.wait_for_termination`）。

```python
# 基线:grpcio==1.60+ (pip install grpcio)。无 proto 环境降级:
# 本例用 aio 内部 API 模拟取消传播;生产用 protoc 生成 stub/server。
import asyncio

async def stream_handler(caller_gone_after: int, total: int) -> None:
    """模拟 grpc.aio 流式 handler:客户端在第 N 条后断开。"""
    sent = 0
    try:
        for i in range(total):
            await asyncio.sleep(0.01)          # 每个 await 都是取消检查点
            sent += 1
            if i == caller_gone_after:
                raise asyncio.CancelledError()  # 模拟 RST_STREAM 到达
    except asyncio.CancelledError:
        print(f"客户端断开:已发送 {sent} 条,未发送 {total - sent} 条")
        raise                                   # 继续向上,框架记 CANCELLED
    finally:
        print("finally: 释放流资源(不做慢操作)")

async def main() -> None:
    try:
        await stream_handler(caller_gone_after=3, total=10)
    except asyncio.CancelledError:
        print("服务端视角: 返回 CANCELLED 给客户端元数据通道已关")

asyncio.run(main())
```

**追问**：
1) deadline 传递链上某一跳忘了传会怎样？——该服务自行新建预算，下游超时独立性破坏：上游已超时取消但下游还在全价跑，取消传播断链；规范是框架层强制透传 metadata（拦截器统一处理），并监控「下游调用时长 > 上游剩余预算」的异常样本。
2) 服务端怎么主动取消自己这边的工作？——`context.cancel()`（grpc.aio 的 ServicerContext）触发本流取消并向客户端发 CANCELLED；内部任务用 `asyncio.shield` 保护的关键段要小心——shield 的任务在流取消后变孤儿，要么显式 await 收尾要么转后台队列登记。
3) 客户端怎么实现「流式 + 优雅关闭」而非粗暴 cancel？——发送 `end-of-stream`（客户端完成发送半边）让服务端收到 half-close 正常收尾；Python 里用 `call.done_writing()`；粗暴 cancel 适合超时兜底，正常结束走协议握手，两者的服务端表现完全不同（CancelledError vs 正常返回）。
