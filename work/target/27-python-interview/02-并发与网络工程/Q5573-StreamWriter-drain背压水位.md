---
title: [Q5573] StreamWriter drain 背压与写缓冲水位控制
date: 2026-11-21
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5573 · StreamWriter drain 背压与写缓冲水位控制

> 难度:★★★★ | 标签:容量规划, asyncio, 背压, StreamWriter

**问**：推送服务往慢客户端发消息，进程内存随时间线性增长直到 OOM。`writer.write()` 不阻塞、`drain()` 才会等——这对组合的内存账怎么算？`write()` 之后不 `await drain()` 会怎样？`drain()` 等的到底是什么水位线，怎么为十万级连接推导每连接写缓冲上限？

**答**：结论：`StreamWriter.write()` 是**纯内存操作**——把数据追加进 `transport` 的写缓冲（`_write_buffer`）并尝试 flush，永不阻塞也不报错；真正背压点是 `await drain()`：它返回的 Future 在缓冲水位降到**低水位线以下**（transport 底层 socket 把待发字节成功发出、`_buffer_size < 256KB 默认低水位？`）前挂起。水位机制：`set_write_buffer_limits(high, low)` 控制两个阈值——缓冲超过 high 暂停"上层数据源"（drain 等待），低于 low 恢复；但注意 high 只影响 drain 的挂起判断，**write 本身无上限**，不 drain 的协程能把缓冲堆到任意大。事故链就是"快生产者 + 慢消费者 + 忘 drain"：生产速率 > socket 发送速率的部分全部堆在每连接写缓冲里，10 万连接 × 每条积压 1MB = 100GB OOM。容量推导方法：每连接写缓冲上限 = 该连接预算内存 / 慢连接比例；工程手段三件套：a) **每条消息 write 后必 drain**（或按批 drain），让背压自然传导到业务生产速率；b) 给 drain 加超时或用 `asyncio.wait_for` 包裹，超时判定为慢连接 → 断开降级（丢弃推送，靠客户端重连拉取）；c) 监控 `transport.get_write_buffer_size()`，按连接聚合 P99 作为容量告警指标——这个数字就是"当前积压字节数"，比进程 RSS 灵敏得多。

```python
# file: code/02_并发与网络工程/q5573_drain_backpressure.py
import asyncio, time, sys

async def main():
    # 服务端 = 慢读者: 消费速率可控(flow 事件), 用于制造确定性的积压/恢复
    flow = asyncio.Event(); flow.set()           # True=允许消费
    async def handler(reader, writer):
        await asyncio.sleep(0.1)                 # 前 0.1s 完全不读 -> 客户端积压
        while True:
            await flow.wait()
            data = await reader.read(1024)       # 1KB/10ms 的慢速消费
            if not data: return
            await asyncio.sleep(0.01)

    srv = await asyncio.start_server(handler, "127.0.0.1", 0)
    r, w = await asyncio.open_connection(*srv.sockets[0].getsockname()[:2])
    import socket as _s
    w.transport.get_extra_info("socket").setsockopt(_s.SOL_SOCKET, _s.SO_SNDBUF, 8192)
    w.transport.set_write_buffer_limits(high=4096, low=1024)
    print("水位线:", w.transport.get_write_buffer_limits())

    chunk = b"x" * 1024
    # 2) 不 drain 狂写: write 永不阻塞, 缓冲无限堆积(事故形态)
    for _ in range(50):
        w.write(chunk)
    print("50 次 write 后积压字节:", w.transport.get_write_buffer_size())

    # 3) 正确形态: 批量 write + await drain, 背压随慢读者传导
    async def paced_writer(n, batch=4):
        for _ in range(0, n, batch):
            for _ in range(batch):
                w.write(chunk)
            await w.drain()                      # 缓冲>high 时在此挂起
    t0 = time.perf_counter()
    await paced_writer(8)
    print("paced 写 8 块 + drain 完成: %.3fs (受慢读者速率约束)" % (time.perf_counter() - t0))

    # 4) drain 加超时: 慢连接识别与降级(停掉消费 -> 积压不被吸收)
    flow.clear()
    for _ in range(100):
        w.write(chunk)
    try:
        await asyncio.wait_for(w.drain(), timeout=0.2)
        print("drain 未超时(内核缓冲吸收了积压, 现实中要结合 get_write_buffer_size 判断)")
    except asyncio.TimeoutError:
        print("drain 超时 -> 判定慢连接, abort 断开降级(积压:", w.transport.get_write_buffer_size(), "B)")
    w.transport.abort()                          # 关慢连接用 abort: 立即丢缓冲
    flow.set()                                   # 放行 handler 读到 EOF
    srv.close()
    await asyncio.sleep(0.1)                     # 残余 handler 由 asyncio.run 收尾取消

asyncio.run(main())
print("容量公式: 进程写缓冲总量 = Σ 各连接 get_write_buffer_size(), P99 告警 + 慢连接踢出")
print("python:", sys.version.split()[0])
```

**追问**：1) `drain()` 到底在等什么条件？——transport 的 `_drain_helper`：当写缓冲高于 high 水位时 transport 把自己标记为 paused，drain 挂起；底层 socket 把数据写入内核缓冲且进程缓冲降到 low 以下后恢复。注意内核 SO_SNDBUF（Q5564）也参与缓冲，所以"drain 返回"不等于"对端已收到"，端到端确认仍要应用层 ACK。2) 高水位设多大合理？——经验起点：单连接 high = 期望最大推送延迟 × 带宽（BDP 的应用层部分），比如 10MBPS 客户端 × 100ms ≈ 125KB；但高水位过大等于纵容积压，推送类服务宁可设小 + 快速踢慢连接，把内存预算让给活跃连接。3) `wait_closed`/连接关闭时积压数据去哪了？——abort() 直接丢弃缓冲并 RST；close() 会尝试冲刷完缓冲再 FIN——**关慢连接要用 abort()**，否则 close 后进程还要背着缓冲等冲刷，是"清理线程反被积压拖死"的常见二次事故。

## 背诵要点
- write() 纯内存不阻塞，背压只在 await drain()：缓冲高于 high 水位挂起、低于 low 恢复；不 drain 的协程可把缓冲堆到 OOM。
- 慢连接治理三件套：每次 write 后（或按批）drain、drain 包 wait_for 超时踢人、监控 get_write_buffer_size() P99。
- 关闭积压连接用 abort()（丢弃缓冲立即 RST），close() 会等冲刷反而被积压拖死；内核 SO_SNDBUF 另有一层缓冲，drain 不等于对端已收。

## 复盘追问
- 你们的推送服务有没有 per-connection 写缓冲指标？OOM 时刻能否回放到哪个连接积压最多？（提示：get_write_buffer_size 定期采样进 metrics，连接级 topN 落日志）
- 群发场景下"一条消息写给 10 万连接"的扇出协程怎么控速？（提示：信号量限并发扇出 + 每扇出 drain，慢连接直接 abort，见 Q5546 每协程内存账联动预算）
