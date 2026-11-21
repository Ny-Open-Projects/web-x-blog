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
