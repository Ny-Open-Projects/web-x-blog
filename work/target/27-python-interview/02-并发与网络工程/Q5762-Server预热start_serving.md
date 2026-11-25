---
title: "[Q5762] asyncio.Server 的 start_serving=False：先 bind 不 listen 的预热窗口"
date: 2026-11-25
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q5762 · asyncio.Server 的 start_serving=False：先 bind 不 listen 的预热窗口

难度：P6 ｜ 标签：asyncio、Server、start_serving、端口绑定、优雅发布、就绪探针

基线：CPython 3.12.2，纯标准库；用 `asyncio.start_server(start_serving=False)` 实测"已 bind、未 listen"时客户端连接的表现。

**问**：服务要在启动时加载 200MB 模型、连数据库、预热缓存，耗时 25 秒。为了不让 LB 在这期间把流量打进来，团队用 `start_serving=False` 先 bind 端口，等预热完再 `start_serving()`。结果发布时 LB 的健康检查连上来一直**超时**，而不是快速失败，健康检查线程被挂住，整个 LB 节点被拖慢；另一个实例预热失败但进程没退出，端口一直 bind 着，发布卡了 40 分钟。`start_serving=False` 到底把服务停在了哪一步？为什么连接是超时而不是 refused？这个窗口应该怎么用？

**答**：

- **结论**：`start_serving=False` 让 `create_server` 完成 **socket 创建 + bind**，但**不调用 `listen()`、也不注册 accept 回调**；所以端口被占住，但内核没有监听队列，客户端发 SYN 后收不到 SYN-ACK，表现是**连接超时/重试**，不是 `ConnectionRefusedError`。等 `await server.start_serving()` 才真正 `listen` 并开始 accept；`serve_forever()` 内部也会先 `start_serving()`。`server.is_serving()` 在窗口期是 `False`，可以作为就绪状态的一部分。
- **取舍**：这个窗口适合"必须先占住端口/继承 fd，但业务还没准备好"的场景（特权端口、systemd socket activation、配合 `SO_REUSEPORT` 的蓝绿发布）。但它对客户端不友好：超时会让 LB/健康检查线程长时间挂起，比直接返回 503 更糟。更好的组合是"端口照常 listen，但应用层返回 503/ready=false"——让连接快速建立、快速失败，LB 能立刻判断不健康；`start_serving=False` 只用于"进程还没完成初始化、连 HTTP 栈都不该接客"的极短窗口，并且必须有**启动超时 watchdog**：超过 N 秒还没 `start_serving` 就退出，避免"bind 着但永远不服务"。
- **实战**：发布脚本在 import 阶段就 bind 443，预热失败后进程停在 `sys.exit` 前的清理逻辑里，端口一直占着；LB 的健康检查用了 30 秒 connect timeout，64 个并发检查把 LB 的工作线程占满。修复：① 把 bind 放到 `main()` 里，预热成功后才 `start_serving`；② 加 `asyncio.wait_for(warmup(), 60)`，失败直接 `os._exit(1)` 释放端口；③ LB 健康检查 connect timeout 降到 2 秒，并且改为"连上后看 `/ready` 状态码"，不再用纯 TCP 探活。发布窗口从 40 分钟降到 90 秒。

下面验证：未 `start_serving` 时 `is_serving()` 为 False、客户端 connect 超时、handler 不执行；`start_serving()` 后同一端口正常接客。

```python
# start_serving=False: 已 bind 未 listen, 连接表现为超时而非 refused
import asyncio


async def main():
    served = []

    async def handler(reader, writer):
        served.append("accepted")
        await reader.read(1024)
        writer.close()
        await writer.wait_closed()

    server = await asyncio.start_server(
        handler, "127.0.0.1", 0, start_serving=False
    )
    port = server.sockets[0].getsockname()[1]
    print("[1] bind 后 is_serving =", server.is_serving(), "port =", port)
    assert server.is_serving() is False

    # 窗口期: 端口被占, 但 connect 超时, handler 不会被调用
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection("127.0.0.1", port), timeout=0.3
        )
        writer.close()
        raise AssertionError("未 start_serving 时不应连接成功")
    except asyncio.TimeoutError:
        print("[2] 窗口期连接 -> TimeoutError（不是 ConnectionRefused）")
    assert served == []

    # 开始接客
    await server.start_serving()
    print("[3] start_serving 后 is_serving =", server.is_serving())
    assert server.is_serving() is True

    reader, writer = await asyncio.open_connection("127.0.0.1", port)
    writer.write(b"ping")
    await writer.drain()
    await asyncio.sleep(0.05)
    print("[4] handler 执行:", served)
    assert served == ["accepted"]

    writer.close()
    await writer.wait_closed()
    server.close()
    await server.wait_closed()
    print("[5] 关闭完成")


asyncio.run(main())
```

**追问一**：`start_serving=False` 时端口真的被占住了吗？其他进程能 bind 吗？—— 能占住。socket 已经 `bind`，只是没 `listen`；同一地址/端口再 `bind` 会因 `EADDRINUSE` 失败（除非双方都设了 `SO_REUSEPORT`）。这正是"预热窗口"能防止别人抢端口的原因，也是"预热失败不退进程"会阻塞发布的原因。要确认端口状态，用 `lsof -i :PORT` 或 `ss -ltn` 看是否有 LISTEN；窗口期可能只有 socket 没有 LISTEN 状态。

**追问二**：`serve_forever()` 和 `start_serving()` 怎么配合？—— `serve_forever()` 会先调用 `start_serving()`，然后挂起直到 `server.close()` 被调用；它返回的 Task 被取消时不会自动关服务器。常见写法是 `await server.start_serving()` 显式控制接客时机，再用 `await server.serve_forever()` 保持主协程存活；两者都调用也安全（`start_serving` 幂等），但不要在 `serve_forever` 之后才 `start_serving`，那时已经在接客了。

## 背诵要点

- `start_serving=False` 完成 bind 但不 listen/accept；窗口期连接表现为超时，`is_serving()` 为 False。
- 适合特权端口/继承 fd/极短预热窗口；对外服务应"listen 但返回 503"，让探针快速失败，而不是让连接挂住。
- 必须有启动超时 watchdog，预热失败就退出释放端口，避免"bind 着永不服务"。

## 复盘追问

- 为什么窗口期的客户端是超时而不是 connection refused？（socket 未 `listen`，内核不回 RST/SYN-ACK，SYN 被丢弃后客户端重试）
- `start_serving=False` 与 `SO_REUSEPORT` 蓝绿发布怎么配合？（先 bind 占住复用组，预热后再 listen；旧实例继续接客，切换时靠内核哈希分流）
