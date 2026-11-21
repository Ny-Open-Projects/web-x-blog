---
title: [Q2409] sendall 与部分发送语义
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2409 · sendall 与部分发送语义

> 难度:★★★ | 标签:send, sendall, 发送缓冲

**问**:send 返回值小于数据长度代表什么?sendall 又保证了什么?

**答**:send 的契约是"接受本次塞进发送缓冲的字节数":缓冲将满时可能只塞一部分,非阻塞模式下塞不进还会抛 BlockingIOError;sendall 则是标准库替你写好的循环,保证全量送进缓冲或抛错。

- 实测:接收方睡 0.3 秒不读、发送缓冲调小,单次 send 对 1MB 只写入 4KB,这就是部分写;

- 手写 my_sendall:send 返回多少记多少,BlockingIOError 时 select 等可写再续,实测续传完成且中途 10 次缓冲满;

- 接收端最终一字不差收全 1MB,验证循环续传的正确性;

- 自己造协议栈时理解这层循环,用高层库时才知道它替你挡了什么。

```python
# file: code/02_并发与网络工程/q2409_sendall_partial.py
# -*- coding: utf-8 -*-
"""sendall 与部分发送: send 只保证"这次塞了多少", sendall 才保证全量。

- 非阻塞 send 在发送缓冲将满时返回部分写入的字节数, 或抛 BlockingIOError;
- 接收方不读、缓冲灌满时, 大块数据必须由调用方循环续传;
- sendall 就是标准库替你写好的这个循环, 自己手写一遍才看得见边界。
"""
import select
import socket
import threading
import time

PAYLOAD = bytes(range(256)) * 4096          # 1MB


def my_sendall(sock, data):
    """非阻塞版 sendall: send 返回多少记多少, 写不进就 select 等可写。"""
    view = memoryview(data)
    sent_total = 0
    sends = 0
    blocked = 0
    while sent_total < len(data):
        try:
            n = sock.send(view[sent_total:])
            sends += 1
            sent_total += n
        except BlockingIOError:
            blocked += 1
            select.select([], [sock], [], 1.0)   # 等发送缓冲腾出空间
    return sent_total, sends, blocked


def main():
    a, b = socket.socketpair()
    a.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)   # 缓冲调小制造背压
    b.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
    a.setblocking(False)

    # 接收方先睡 0.3s 不读, 发送缓冲很快灌满
    got = []

    def reader():
        time.sleep(0.3)
        b.settimeout(5)
        total = 0
        while total < len(PAYLOAD):
            chunk = b.recv(65536)
            if not chunk:
                break
            got.append(chunk)
            total += len(chunk)

    rt = threading.Thread(target=reader)
    rt.start()
    time.sleep(0.05)                 # 确保接收方已在睡, 没人读

    first = a.send(PAYLOAD)          # 单次 send 的语义: 能塞多少塞多少
    print("单次 send 返回: %d / %d 字节" % (first, len(PAYLOAD)))
    assert first < len(PAYLOAD), "缓冲背压下单次 send 必然只能部分写入"

    sent, sends, blocked = my_sendall(a, PAYLOAD[first:])
    print("my_sendall 续传完成: 共 %d 字节, %d 次 send, %d 次缓冲满" %
          (first + sent, sends, blocked))
    assert first + sent == len(PAYLOAD)
    rt.join(timeout=6)
    assert b"".join(got) == PAYLOAD, "接收端必须一字不差地收全"


if __name__ == "__main__":
    main()
```

**追问**:1) sendall 在什么情况下也会失败?——对端中途关闭、超时或缓冲持续不可写,此时已发送部分不可回滚,协议设计要考虑重连重传。2) 非阻塞下 select 等可写要不要限次?——要,加总超时预算,否则慢接收者把发送方钉死。3) 部分写的完整契约与 sendall 的边界?——send 返回「本次塞进发送缓冲的字节数」;缓冲满+非阻塞=BlockingIOError;sendall=标准库写好的循环(全量入缓冲或抛错)——sendall 失败时已发送部分不可回滚(对端可能收到一半),协议设计要重连重传。4) 手写 send 循环的工程要点?——send 返回多少记多少;BlockingIOError 时 select 等可写再续;加总超时预算(慢接收者钉死发送方,Q2144 同源);记账推进 offset——「循环+记账+预算」是发送侧的完整边界。5) 生产陷阱?——send 返回值不看(丢数据);sendall 配 SO_SNDTIMEO(中途超时半截);非阻塞 send 无 select(忙等);无总预算(永久阻塞);把 sendall 当「保证送达」(只保证入缓冲,不保证对端收到);大文件发送无分块进度(超时无法定位)。

---
