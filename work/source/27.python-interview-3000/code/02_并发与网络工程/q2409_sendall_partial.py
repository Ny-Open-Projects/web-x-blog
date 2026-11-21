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
