---
title: [Q586] 异步连接池:acquire/release 的完整实现
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q586 · 异步连接池:acquire/release 的完整实现

> 难度:★★★★ | 标签:连接池, asyncio, 资源管理

**问**:自己实现一个 asyncio 连接池,要处理哪些问题?

**答**:四个关键点:上限控制用 Semaphore(拿不到许可就排队,而不是无限新建);空闲连接用 asyncio.Queue 存放,acquire 优先取空闲、没有才新建,release 归还;连接有效性要校验——空闲期间的断连要能检测(简单的做法是归还时标记年龄,取出时超龄就丢弃重建);生命周期收尾要在池关闭时排空并关闭所有连接。生产级还要加:按目标地址分池、健康检查、获取超时。下面实现核心版并配合 echo 服务验证"复用而不是新建"。

```python
# file: code/02_并发与网络工程/q586_async_pool.py
import asyncio
import time


class AsyncConnPool:
    def __init__(self, host: str, port: int, size: int = 3) -> None:
        self._host, self._port, self._size = host, port, size
        self._idle: asyncio.Queue = asyncio.Queue()
        self._sem = asyncio.Semaphore(size)  # 上限控制
        self._created = 0
        self._reused = 0

    async def acquire(self):
        await self._sem.acquire()
        try:
            conn = self._idle.get_nowait()
            self._reused += 1
            return conn
        except asyncio.QueueEmpty:
            reader, writer = await asyncio.open_connection(self._host, self._port)
            self._created += 1
            return reader, writer

    def release(self, conn) -> None:
        self._idle.put_nowait(conn)
        self._sem.release()

    def discard(self, conn) -> None:
        _reader, writer = conn
        writer.close()
        self._sem.release()

    async def close_all(self) -> None:
        while not self._idle.empty():
            _r, w = self._idle.get_nowait()
            w.close()
            await w.wait_closed()


async def echo_server(reader, writer) -> None:
    try:
        while True:
            data = await reader.read(100)
            if not data:
                break
            writer.write(data)
            await writer.drain()
    finally:
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


async def do_request(pool: AsyncConnPool, msg: str) -> str:
    conn = await pool.acquire()
    try:
        reader, writer = conn
        writer.write(msg.encode())
        await writer.drain()
        data = await asyncio.wait_for(reader.read(100), 1.0)
        pool.release(conn)
        return data.decode()
    except Exception:
        pool.discard(conn)  # 出错的连接不回池
        raise


async def main() -> None:
    server = await asyncio.start_server(echo_server, "127.0.0.1", 0)
    port = server.sockets[0].getsockname()[1]
    pool = AsyncConnPool("127.0.0.1", port, size=3)

    results = await asyncio.gather(*[do_request(pool, f"req{i}") for i in range(10)])
    print("请求结果:", results)
    print(f"新建连接 {pool._created} 次, 复用 {pool._reused} 次 (10 个请求)")
    await pool.close_all()
    server.close()
    await server.wait_closed()


asyncio.run(main())
```

**追问**:1) 怎么发现"池里的连接已被对端断开"?——取出时做轻量探活(非阻塞 peek 或发 ping),或对 read 抛 ConnectionResetError 的连接静默重建一次再失败上抛。2) 池的完整契约?——acquire 超时(防饿死)、归还校验(reset)、坏连接销毁、空闲回收(存活期)、池上限背压;租借计数与泄漏检测(Q1284)。3) 与异步的配合?——Semaphore 限并发窗口(Q595);acquire 等待队列;shutdown 排空(Q614)。4) 生产陷阱?——忘记归还(池耗尽);归还脏连接污染下家;无空闲回收被 NAT/防火墙断链;探活本身阻塞循环。

---
