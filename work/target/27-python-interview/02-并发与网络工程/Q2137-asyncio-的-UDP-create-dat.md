---
title: [Q2137] asyncio 的 UDP:create_datagram_endpoint
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2137 · asyncio 的 UDP:create_datagram_endpoint

> 难度:★★★★ | 标签:UDP, datagram, 无连接

**问**:asyncio 下 UDP 怎么写?和 TCP 的模型差在哪?

**答**:create_datagram_endpoint 返回 transport 与协议对象,sendto 直接指定目的地,datagram_received 异步收包,没有连接建立与断开。

- 回环实测:客户端发 ping 收 ack,一条"端点"撑完请求应答;

- 无连接的代价是没有内建顺序与重传,应用层要自己补;

- error_received 是传输层异步错误(如 ICMP 端口不可达)的出口;

- on_con_lost Future 是收尾锚点,close 后等待它完成清理。

```python
# file: code/02_并发与网络工程/q2137_datagram_endpoint.py
# -*- coding: utf-8 -*-
"""asyncio 的 UDP: create_datagram_endpoint 无连接端点。

- DatagramEndpoint 用协议类收发, sendto 直接指定目的地, 无握手;
- on_con_lost Future 是收尾锚点, error 属性暴露传输层错误;
- 回环上一对端点即可演示请求/应答, 无需listen/accept那套流程。
"""
import asyncio

HOST = "127.0.0.1"


class EchoServer(asyncio.DatagramProtocol):
    def __init__(self):
        self.received = []

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        self.received.append((data, addr))
        self.transport.sendto(b"ack:" + data, addr)


class EchoClient(asyncio.DatagramProtocol):
    def __init__(self, on_con_lost):
        self.on_con_lost = on_con_lost
        self.queue = asyncio.Queue()
        self.error = None

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data, addr):
        self.queue.put_nowait(data)

    def error_received(self, exc):
        self.error = exc            # ICMP 端口不可达等异步错误在这里冒出

    def connection_lost(self, exc):
        if exc:
            self.error = exc
        self.on_con_lost.set_result(True)


async def main():
    loop = asyncio.get_event_loop()
    server_transport, server = await loop.create_datagram_endpoint(
        EchoServer, local_addr=(HOST, 0))
    sport = server_transport.get_extra_info("sockname")[1]
    print("服务端绑定回环临时端口:", sport)

    lost = loop.create_future()
    client_transport, client = await loop.create_datagram_endpoint(
        lambda: EchoClient(lost), remote_addr=(HOST, sport))

    for i in range(3):
        msg = ("ping-%d" % i).encode()
        client_transport.sendto(msg)
        reply = await asyncio.wait_for(client.queue.get(), 2.0)
        print("客户端发出 %s, 收到 %s" % (msg.decode(), reply.decode()))

    print("服务端收到条数:", len(server.received), "-> 无连接, 无握手建连")
    client_transport.close()
    await asyncio.wait_for(lost, 2.0)
    print("客户端 error:", client.error, "| 传输层错误走 error_received")
    server_transport.close()


if __name__ == "__main__":
    asyncio.run(main())
```

**追问**:1) UDP 端点能"连"吗?——可以带 remote_addr 创建,之后 sendto 不写地址也行,但那只是地址默认值,语义仍是无连接。2) datagram_received 里做重活会怎样?——事件循环被拖住,所有端点一起卡;重活立刻丢队列或 to_thread。3) UDP 端点的应用层责任清单?——顺序(按包重组 Q1868)、重传(超时重发 Q1867)、去重(序号台账 Q1607)、分片(单包 ≤MTU,大消息应用层切)——asyncio 只给「收发原语」,可靠传输全是应用层的事。4) error_received 的语义与用途?——传输层异步错误出口:ICMP port unreachable 回灌(Q1314 同源)、超 MTU 等;不处理时错误静默;「发了没回应」的第一排查点是 error_received 有没有被触发。5) 生产陷阱?——datagram_received 里做重活(堵循环,见原问);on_con_lost 没 await(收尾泄漏);sendto 高频小包(Nagle 无关,但内核缓冲/速率要限);把 remote_addr 当「已连接」(仍无连接语义);忽略 error_received(错误黑洞)。

---
