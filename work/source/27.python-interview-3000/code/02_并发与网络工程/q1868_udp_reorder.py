# -*- coding: utf-8 -*-
"""UDP 乱序到达重组: 按序号缓存, 只交付连续前缀, 缺口暂存等补齐。

- 乱序中间人把 6 个分块按倒序转发, 模拟真实网络的乱序投递;
- 接收方维护 expected 游标: 到达序号等于游标立即交付并冲洗缓存;
- 序号超前则暂存缺口之后的数据, 缺口补上后一次性按序放行。
"""
import socket
import threading

CHUNKS = 6
MESSAGE = b"HELLO-UDP-REORDER-DEMO"


def split_message():
    base = len(MESSAGE) // CHUNKS
    rem = len(MESSAGE) % CHUNKS
    out = []
    pos = 0
    for i in range(CHUNKS):
        n = base + (1 if i < rem else 0)
        out.append(MESSAGE[pos:pos + n])
        pos += n
    return out


def port_of(s):
    return s.getsockname()[1]


def start_receiver(done_event, result_box):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 0))

    def loop():
        expected = 0
        buffer = {}
        delivered = b""
        sock.settimeout(3.0)
        while expected < CHUNKS:
            data, _ = sock.recvfrom(2048)
            seq = data[0]
            payload = data[1:]
            if seq == expected:
                delivered += payload
                print("  交付 seq=%d(连续)" % seq)
                expected += 1
                while expected in buffer:              # 冲洗暂存区
                    delivered += buffer.pop(expected)
                    print("  冲洗暂存 seq=%d" % expected)
                    expected += 1
            else:
                buffer[seq] = payload
                print("  暂存 seq=%d, 缺口在 seq=%d" % (seq, expected))
        result_box.append(delivered)
        done_event.set()

    threading.Thread(target=loop, daemon=True).start()
    return sock


def start_reorderer(recv_port):
    """乱序中间人: 收齐全部分块后按倒序转发给真正的接收端。"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("127.0.0.1", 0))
    collected = {}

    def loop():
        sock.settimeout(3.0)
        while len(collected) < CHUNKS:
            data, _ = sock.recvfrom(2048)
            collected[data[0]] = data[1:]
        for seq in sorted(collected, reverse=True):    # 倒序转发, 制造乱序
            sock.sendto(bytes([seq]) + collected[seq], ("127.0.0.1", recv_port))

    threading.Thread(target=loop, daemon=True).start()
    return sock


def main():
    done = threading.Event()
    result_box = []
    recv_sock = start_receiver(done, result_box)
    reorder_sock = start_reorderer(port_of(recv_sock))

    cli = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    chunks = split_message()
    for i, chunk in enumerate(chunks):
        cli.sendto(bytes([i]) + chunk, ("127.0.0.1", port_of(reorder_sock)))
    cli.close()

    assert done.wait(timeout=3.0), "3 秒内应完成重组"
    recv_sock.close()
    reorder_sock.close()

    got = result_box[0]
    print("乱序交付后重组结果:", got.decode())
    assert got == MESSAGE, "按序号重组必须还原原文"
    print("结论: 乱序不可怕, 缺序号先暂存, 游标推进时连续放行")


if __name__ == "__main__":
    main()
