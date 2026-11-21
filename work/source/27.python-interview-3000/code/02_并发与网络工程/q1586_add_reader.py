"""add_reader / add_writer: 不写协程也能用事件循环。

事件循环的底座是 fd 级回调:
- add_reader(fd, cb): fd 可读时在循环线程里跑 cb;
- add_writer(fd, cb): fd 可写时跑 cb, 写完必须 remove_writer, 否则
  选择器持续报告可写 -> 回调空转烧 CPU;
- 回调必须是纯非阻塞的: send/recv 遇 BlockingIOError 直接返回。
"""
import asyncio
import socket
from collections import deque


async def main():
    loop = asyncio.get_running_loop()
    a, b = socket.socketpair()          # 本机双向管道, 当作最小"网络"
    a.setblocking(False)
    b.setblocking(False)

    outbox = deque([b"ping-1", b"ping-2", b"ping-3"])
    echoed = bytearray()
    expected = sum(len(x) for x in outbox)
    done = loop.create_future()

    def on_readable():
        try:
            data = b.recv(4096)
        except BlockingIOError:
            return
        if data:
            echoed.extend(data)         # 三次 send 可能被合并成一次 recv
            if len(echoed) >= expected:
                loop.remove_reader(b.fileno())
                if not done.done():
                    done.set_result(None)

    def on_writable():
        while outbox:
            try:
                sent = a.send(outbox[0])
            except BlockingIOError:
                return                  # 缓冲区满: 等下一轮可写
            if sent == len(outbox[0]):
                outbox.popleft()
            else:
                outbox[0] = outbox[0][sent:]
        loop.remove_writer(a.fileno())  # 发完注销, 防空转

    loop.add_reader(b.fileno(), on_readable)
    loop.add_writer(a.fileno(), on_writable)
    await asyncio.wait_for(done, timeout=3.0)
    loop.remove_reader(b.fileno())
    print("fd 回调累计收到:", bytes(echoed))
    assert bytes(echoed) == b"ping-1ping-2ping-3", "三条消息都应经回调送达"
    print("注意: 三次 send 在对端被合并成一次 recv——fd 回调不保消息边界")
    a.close()
    b.close()
    print("结论: 协程只是 fd 回调的糖; 回调注册/注销配对是 fd 级编程的生命线")


if __name__ == "__main__":
    asyncio.run(main())
